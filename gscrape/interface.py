import pyppeteer
from typing import  List, Union
from gscrape.utils import inner_text_all, inner_text, hideAutomation
import gscrape.patches
from urllib.parse import urlparse
from gscrape.elements import SerpBlock


class SearchInterface():   

    def __init__(self, url: str, lat: Union[None, float], long: Union[float, None], graphical:bool, proxy: Union[None, str]):
        gscrape.patches.disable_timeout()
        gscrape.patches.add_geolocation()
        gscrape.patches.add_permissions()
        self.browser = None
        self.url = url
        self.lat = lat
        self.long = long
        self.graphical = graphical
        self.proxy = None
        if proxy is not None:
            self.proxy = urlparse(proxy)

    async def launch(self):
        chrome_args = [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-infobars',
        '--window-position=0,0',
        '--ignore-certifcate-errors',
        '--ignore-certifcate-errors-spki-list',
        '--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3312.0 Safari/537.36"'
        ]
        if self.proxy is not None and self.proxy.scheme is not None:
            chrome_args.append(f'--proxy-server={self.proxy.scheme}://{self.proxy.hostname}:{self.proxy.port}')
        self.browser = await pyppeteer.launch({'headless':not self.graphical, 'slowMo': 20 if self.graphical else 0}, args=chrome_args)


    
    async def _init(self, queryterm) -> pyppeteer.page.Page:
        if self.browser is None:
            raise TypeError("browser was not launched yet. Please call launch() before.")
        context = await self.browser.createIncognitoBrowserContext()  
        
        page = await context.newPage()  
        await page.emulate(viewport = {'width': 1280, 'height': 960})
        if self.proxy is not None and self.proxy.username is not None and self.proxy.password is not None:
            await page.authenticate({'username':self.proxy.username, 'password': self.proxy.password})
        await hideAutomation(page) 
        if self.long is not None:  
            await context.overridePermissions(self.url, ['geolocation'])
            await page.setGeolocation(self.long, self.lat, 10)  
            await page.reload()    
        await page.goto(self.url)  
        await page.keyboard.type(queryterm,  {'delay':0})  
        await page.waitForFunction("""() => {
            nodes = document.getElementsByClassName('sbl1');
            return nodes.length > 1;
        }""")
        return page
    

    async def serp(self, queryterm) -> List:
        page = await self._init(queryterm)
        await page.keyboard.press('Enter')
        return await self._scrape_serp(page)


    async def autocomplete(self, queryterm) -> List[str]:
        page = await self._init(queryterm)
        completions = await inner_text_all(page, '.sbl1')
        completions = [el for el in completions if el != ""]
        await page.close()
        return completions

    async def _scrape_serp(self, page):
        await page.waitForFunction("""()=>{
            loc = document.getElementById('Wprf1b');
            return loc != null && loc.innerText != "";
        }""")
        results = []
        results.append({'stats': await inner_text(page, "#resultStats")})
        results.append({'appbar': await inner_text_all(page, ".appbar .title")})
        blocks = await page.querySelectorAll('.bkWMgd')
        for block in blocks:
            elem = await SerpBlock.get_instance(block)
            results.append(await elem.scrape())
        results.append({'suggestions': await inner_text_all(page, '#brs a')})
        results.append({'location': await inner_text(page, '#Wprf1b')})    
        return results
 
