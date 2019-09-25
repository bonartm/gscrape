import pyppeteer
from typing import List
import gscrape.serp


class SearchInterface():

    def __init__(self, browser: pyppeteer.browser.Browser, url):
        self.browser = browser
        self.url = url

    async def _init(self, queryterm) -> pyppeteer.page.Page:
        context = await self.browser.createIncognitoBrowserContext()
        page = await context.newPage()
        await page.goto(self.url)
        await page.keyboard.type(queryterm,  {'delay':0})     
        await page.waitFor(500)
        return page
    
    async def serp(self, queryterm) -> gscrape.serp.GoogleSerp:
        page = await self._init(queryterm)
        await page.keyboard.press('Enter')
        return gscrape.serp.GoogleSerp(page)

    async def autocomplete(self, queryterm) -> List[str]:
        page = await self._init(queryterm)
        completions = await page.querySelectorAllEval('.sbl1', 'nodes => nodes.map(node => node.innerText)')
        completions = [el for el in completions if el != ""]
        await page.close()
        return completions
 
