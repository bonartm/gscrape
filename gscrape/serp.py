import pyppeteer
from typing import List, Dict, Callable, Optional
from gscrape.elements import SerpBlock
import asyncio

def _catch_missing_elem(fun: Callable) -> Callable:
    async def handler(*args, **kwargs):
        try:
            return await fun(*args, **kwargs)
        except pyppeteer.errors.ElementHandleError:
            return None
    return handler


class GoogleSerp:

    def __init__(self, page: pyppeteer.page.Page):
        self.page = page

    async def scrape(self):
        await self.page.waitFor(500)
        await self.page.waitForSelector('#Wprf1b')

        results = []
        results.append({'stats': await self._stats()})
        blocks = await self.page.querySelectorAll('.bkWMgd')
        for block in blocks:
            elem = await SerpBlock.get_instance(block)
            results.append(await elem.scrape())

        results.append({
            'suggestions': await self._suggestions(),
            'location': await self._location()})
        return results        

    @_catch_missing_elem
    async def _stats(self) -> Optional[str]:
        return await self.page.querySelectorEval('#resultStats', 'node => node.innerText')
       
    @_catch_missing_elem
    async def _location(self) -> Optional[str]:
        return await self.page.querySelectorEval('#Wprf1b', 'node => node.innerText')

    @_catch_missing_elem
    async def _suggestions(self) -> Optional[List[str]]:
        return await self.page.querySelectorAllEval('#brs a', 'nodes => nodes.map(node => node.innerText)')


    



    

       

    

    