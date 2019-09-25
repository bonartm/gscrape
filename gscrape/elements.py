from sys import platform
from pyppeteer.element_handle import ElementHandle
from typing import List, Dict, Any
from pyppeteer.errors import ElementHandleError
import abc
from abc import abstractmethod


class SerpBlock(abc.ABC):
    @classmethod
    async def get_instance(cls, block: ElementHandle) -> 'SerpBlock':
        classes = cls.__subclasses__()
        for cl in classes:
                # test if element exists in page and return correct object
                elem = await block.querySelector(cl.selector)
                if elem is not None:
                    return cl(block)
        return NotImplemented(block)   

    selector=None       
    
    def __init__(self, block: ElementHandle):
        self.block= block 

    async def inner_text(self, selector: str) ->  List[str]:
        return await self.block.querySelectorAllEval(selector, 'nodes => nodes.map(node => node.innerText)')

    async def inner_attribute(self, selector: str, attribute = 'href'):
        return await self.block.querySelectorAllEval(selector, f'nodes => nodes.map(node => node.getAttribute("{attribute}"))')

    @abstractmethod
    async def scrape(self):
        pass


class NotImplemented(SerpBlock):
    async def scrape(self):
        return {"NA": None}

class PeopleAsk(SerpBlock):
    selector = '.related-question-pair'
    async def scrape(self):
        questions = await self.inner_text('.related-question-pair')
        return {"peopleasked": questions}

class Images(SerpBlock):
    selector = '.YDJP6c'
    async def scrape(self):
        links = await self.inner_attribute('img', 'title')
        sources = await self.inner_attribute('img', 'src')
        return {"images": [{"url": links[i], "imgsrc": sources[i]} for i in range(len(links))]}


class InstantAnswer(SerpBlock):
    selector = '.ifM9O'
    async def scrape(self):
        return {"instantanswer": None}

class Videos(SerpBlock):
    selector = '.P94G9b'
    async def scrape(self):
        links = await self.inner_attribute('g-inner-card a')
        title = await self.inner_text('.wCIBKb')
        source = await self.inner_text('.RgAZAc')
        platform = await self.inner_text('.nHGuld .zECGdd')
        time = [el.split("-")[1] for el in platform]
        platform = [el.split("-")[0] for el in platform]
        return {'videos': [{
            'url':links[i],
            'title': title[i], 
            'source':source[i], 
            'time':time[i], 
            'platform':platform[i]} for i in range(len(links))]} 

class OrganicResults(SerpBlock):    
    selector = '.rc'    
    async def scrape(self):
        links = await self.inner_attribute('.rc .r > a')
        titles = await self.inner_text('.ellip')
        snippets = await self.inner_text('.st')
        
        return {'organic': [{
            'url':links[i],
            'title': titles[i], 
            'snippets':snippets[i]} for i in range(len(links))]}

class NewsCarousel(SerpBlock):
    selector = '.So9e7d'
    async def scrape(self):
        links = await self.inner_attribute('.So9e7d a')
        source = await self.inner_text('.So9e7d cite')
        time = await self.inner_text('.So9e7d .f')
        title = await self.inner_text('.nDgy9d')
        return {'topstories_carousel': [{
            'title': title[i], 
            'url':links[i], 
            'source':source[i], 
            'time':time[i]} for i in range(len(links))]} 


class NewsCards(SerpBlock):
    selector = '.qmv19b'
    async def scrape(self):
        links = await self.inner_attribute('.dbsr a')
        source = await self.inner_text('.wqg8ad')
        time = await self.inner_text('.FGlSad span')
        title = await self.inner_text('.nDgy9d')
        return {'topstories_cards': [{
            'title': title[i], 
            'url':links[i], 
            'source':source[i], 
            'time':time[i]} for i in range(len(links))]} 
