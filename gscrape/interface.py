import pyppeteer
from typing import List
import gscrape.serp
from gscrape.utils import inner_text_all, hideAutomation


class SearchInterface():

    def __init__(self, browser: pyppeteer.browser.Browser, url: str, lat: float, long: float):
        self.browser = browser
        self.url = url
        self.lat = lat
        self.long = long

    async def _init(self, queryterm) -> pyppeteer.page.Page:
        context = await self.browser.createIncognitoBrowserContext()
        await context.overridePermissions(self.url, ['geolocation'])
        page = await context.newPage()  
        await hideAutomation(page) 
        await page.setGeolocation(self.long, self.lat, 10)     
        await page.goto(self.url)  
        await page.reload()    
        await page.keyboard.type(queryterm,  {'delay':0})  
        await page.waitForFunction("""() => {
            nodes = document.getElementsByClassName('sbl1');
            return nodes.length > 1;
        }""")
        return page
    
    async def serp(self, queryterm) -> gscrape.serp.GoogleSerp:
        page = await self._init(queryterm)
        await page.keyboard.press('Enter')
        return gscrape.serp.GoogleSerp(page)

    async def autocomplete(self, queryterm) -> List[str]:
        page = await self._init(queryterm)
        completions = await inner_text_all(page, '.sbl1')
        completions = [el for el in completions if el != ""]
        await page.close()
        return completions
 
