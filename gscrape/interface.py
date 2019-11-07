import random
from typing import List, Union
from urllib.parse import urlparse
import pyppeteer
from gscrape.utils import inner_text_all, inner_text, hideAutomation
import gscrape.patches
from gscrape.elements import SerpBlock
from gscrape.db import GoogleMongo


class SearchInterface():
    """Controls a headless browser to fetch SERPs or autocompletions"""

    async def __aenter__(self):
        user_agent = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
                      "(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
        chrome_args = [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-infobars',
            '--window-position=0,0',
            '--ignore-certifcate-errors',
            '--ignore-certifcate-errors-spki-list',
            f'--user-agent={user_agent}'
        ]
        if self.proxy.scheme is not None and self.proxy.hostname is not None:
            url = f'{self.proxy.scheme}://{self.proxy.hostname}:{self.proxy.port}'
            chrome_args.append(f'--proxy-server={url}')
        self.browser = await pyppeteer.launch({
            'headless': not self.graphical,
            'slowMo': 20 if self.graphical else 0}, args=chrome_args)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.browser is not None:
            await self.browser.close()

    def __init__(self, url: str,
                 lat: Union[None, float], lon: Union[float, None],
                 graphical: bool,
                 proxy: Union[None, str],
                 mongo_uri: Union[None, str]):
        gscrape.patches.disable_timeout()
        gscrape.patches.add_permissions()
        gscrape.patches.add_geolocation()
        self.browser = None
        self.url = url
        self.lat = lat
        self.lon = lon
        self.graphical = graphical
        self.mongo = None
        if mongo_uri is not None:
            self.mongo = GoogleMongo(mongo_uri)
        self.proxy = urlparse(proxy)

    async def _init(self, queryterm) -> pyppeteer.page.Page:
        if self.browser is None:
            raise TypeError(
                "Browser was not launched yet. Please use the 'async with' syntax."
            )
        context = await self.browser.createIncognitoBrowserContext()
        page = await context.newPage()
        await page.emulate(viewport={'width': 1280, 'height': 960})
        if self.proxy.username is not None and self.proxy.password is not None:
            await page.authenticate({
                'username': self.proxy.username,
                'password': self.proxy.password})
        await hideAutomation(page)
        if self.lon is not None:
            await context.overridePermissions(self.url, ['geolocation'])
            await page.setGeolocation(self.lon, self.lat, 10)
        await page.goto(self.url)
        if self.lon is not None:
            await page.reload()
        await page.keyboard.type(queryterm, {'delay': random.randint(1, 20)})
        await page.waitForFunction("""() => {
            nodes = document.getElementsByClassName('sbl1');
            return nodes.length > 1;
        }""")
        return (page, context)

    async def serp(self, queryterm) -> List:
        """returns a list of a parsed search result page"""
        page, context = await self._init(queryterm)
        await page.keyboard.press('Enter')
        serp = await self._scrape_serp(page)
        if self.mongo is not None:
            self.mongo.save_serp(queryterm, self.proxy, self.lat, self.lon, self.graphical, serp)
        await context.close()
        return serp

    async def autocomplete(self, queryterm) -> List[str]:
        """returns a list of autocompletions"""
        page, context = await self._init(queryterm)
        completions = await inner_text_all(page, '.sbl1')
        completions = [el for el in completions if el != ""]
        await context.close()
        return completions

    async def _scrape_serp(self, page):
        await page.waitForFunction("""()=>{
            loc = document.getElementById('Wprf1b');
            return loc != null && loc.innerText != "";
        }""")
        results = {}
        results.update({
            'stats': await inner_text(page, "#resultStats"),
            'appbar': await inner_text_all(page, ".appbar .title"),
            'suggestions': await inner_text_all(page, '#brs a'),
            'location': await inner_text(page, '#Wprf1b')
        })
        blocks = await page.querySelectorAll('.bkWMgd')
        results['elements'] = []
        for block in blocks:
            elem = await SerpBlock.get_instance(block)
            results['elements'].append(await elem.scrape())
        return results
