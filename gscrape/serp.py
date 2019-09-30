import pyppeteer
from typing import List, Dict, Callable, Optional
from gscrape.elements import SerpBlock
import asyncio
from gscrape.utils import inner_text_all, inner_text

class GoogleSerp:

    def __init__(self, page: pyppeteer.page.Page):
        self.page = page

    async def scrape(self):
        await self.page.waitForFunction("""()=>{
            loc = document.getElementById('Wprf1b');
            return loc != null && loc.innerText != "";
        }""")

        results = []
        results.append({
            'stats': await inner_text(self.page, "#resultStats"),
            'appbar': await inner_text_all(self.page, ".appbar .title")})

        blocks = await self.page.querySelectorAll('.bkWMgd')
        for block in blocks:
            elem = await SerpBlock.get_instance(block)
            results.append(await elem.scrape())

        results.append({
            'suggestions': await inner_text_all(self.page, '#brs a'),
            'location': await inner_text(self.page, '#Wprf1b')})
        return results
            