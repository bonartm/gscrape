import abc
from abc import abstractmethod
from typing import Union, List
from pyppeteer.element_handle import ElementHandle
from gscrape.utils import (to_dict, inner_attribute, inner_attribute_all,
                           inner_text, inner_text_all)


class SerpBlock(abc.ABC):
    """Abstract base class for a result page object"""
    @classmethod
    async def get_instance(cls, block: ElementHandle) -> 'SerpBlock':
        """
        Factory function that assigns the correct child class to a serp block
        """
        classes = cls.__subclasses__()
        for child in classes:
            elem = await block.querySelector(child.selector)
            if elem is not None:
                return child(block)
        return UnknownElement(block)

    selector = None

    def __init__(self, block: ElementHandle):
        self.block = block

    @abstractmethod
    async def scrape(self) -> Union[str, List[str]]:
        """Transforms a SERP block into a structured list"""
        pass


class UnknownElement(SerpBlock):
    """Indicates that this SERP element is not yet implemented"""
    async def scrape(self):
        return {"NA": None}


class PeopleAsk(SerpBlock):
    """People also ask box"""
    selector = '.related-question-pair'

    async def scrape(self):
        questions = await inner_text_all(self.block, '.related-question-pair')
        return {"peopleasked": questions}


class Images(SerpBlock):
    """Image carousel"""
    selector = '.YDJP6c'

    async def scrape(self):
        urls = await inner_attribute_all(self.block, 'img', 'title')
        sources = await inner_attribute_all(self.block, 'img', 'src')
        return {"images": to_dict(
            url=urls, source=sources
        )}


class InstantAnswer(SerpBlock):
    """Instant answer box"""
    selector = '.ifM9O'

    async def scrape(self):
        return {"instantanswer": await inner_text(self.block, '.Z0LcW')}


class Videos(SerpBlock):
    """Videos carousel"""
    selector = '.P94G9b'

    async def scrape(self):
        urls = await inner_attribute_all(self.block, 'g-inner-card a')
        titles = await inner_text_all(self.block, '.wCIBKb')
        sources = await inner_text_all(self.block, '.RgAZAc')
        platforms = await inner_text_all(self.block, '.nHGuld .zECGdd')
        times = [el.split("-")[1] for el in platforms]
        platforms = [el.split("-")[0] for el in platforms]
        return {"videos": to_dict(
            url=urls, title=titles, source=sources,
            platform=platforms, time=times)}


class OrganicResults(SerpBlock):
    """Organic search results"""
    selector = '.rc'

    async def scrape(self):
        urls = await inner_attribute_all(self.block, '.rc .r > a:nth-of-type(1)')
        titles = await inner_text_all(self.block, '.LC20lb')
        snippets = await inner_text_all(self.block, '.st')
        return {"organic": to_dict(
            url=urls, title=titles, snippet=snippets)}


class NewsCarousel(SerpBlock):
    """News Carousel"""
    selector = '.So9e7d'

    async def scrape(self):
        urls = await inner_attribute_all(self.block, '.So9e7d a')
        sources = await inner_text_all(self.block, '.So9e7d cite')
        times = await inner_text_all(self.block, '.So9e7d .f')
        titles = await inner_text_all(self.block, '.nDgy9d')
        return {'topstories_carousel': to_dict(
            title=titles, url=urls, source=sources, time=times)}


class NewsCards(SerpBlock):
    """News cards element"""
    selector = '.qmv19b'

    async def scrape(self):
        urls = await inner_attribute_all(self.block, '.dbsr a')
        sources = await inner_text_all(self.block, '.wqg8ad')
        times = await inner_text_all(self.block, '.FGlSad span')
        titles = await inner_text_all(self.block, '.nDgy9d')
        return {'topstories_cards': to_dict(
            title=titles, url=urls, source=sources, time=times)}


class TwitterCarousel(SerpBlock):
    """Twitter carousel"""
    selector = '.rQgnxe'

    async def scrape(self):
        title = await inner_text(self.block, '.zTpPx a')
        url = await inner_attribute(self.block, '.zTpPx a')
        tweets = await inner_text_all(self.block, '.YBEXSb')
        times = await inner_text_all(self.block, '.f')
        tweet_urls = await inner_attribute_all(self.block, '.YBEXSb > a')
        return {'twitter_carousel': {
            "title": title, "url": url, "tweets": to_dict(
                tweet=tweets, url=tweet_urls, time=times
            )}}


class Maps(SerpBlock):
    """Google maps element"""
    selector = '.xERobd'

    async def scrape(self):
        return {'maps': None}
