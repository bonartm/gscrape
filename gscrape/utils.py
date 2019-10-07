from typing import Callable, List, Any, Union
from pyppeteer.element_handle import ElementHandle
from pyppeteer.page import Page
from pyppeteer.errors import ElementHandleError
import logging
import pyppeteer
import importlib.resources as pkg_resources
import gscrape.scripts


def _catch_missing_elem(fun: Callable) -> Callable:
    async def handler(*args, **kwargs):
        try:
            return await fun(*args, **kwargs)
        except ElementHandleError:
            logging.warn(f"Element does not exist")
            return None
    return handler

def save_list_get(l, idx, default=None):
    try:
        return l[idx]
    except IndexError:
        logging.warn(f"Index {idx} does not exist in list {l}")
        return default

def to_dict(**kwargs: List[Any]):
    n = len(next(iter(kwargs.values())))
    res = []
    for i in range(n):
        res.append({
            key:save_list_get(value, i) for key, value in kwargs.items()
        })
    return res


@_catch_missing_elem
async def inner_text(node: Union[ElementHandle, Page], selector: str) ->  str:    
    return await node.querySelectorEval(selector, 'node => node.innerText.normalize("NFKC")')


@_catch_missing_elem
async def inner_attribute(node: Union[ElementHandle, Page], selector: str, attribute = 'href') ->  str:
    return await node.querySelectorEval(selector, f'node => node.getAttribute("{attribute}")')


@_catch_missing_elem
async def inner_text_all(node: Union[ElementHandle, Page], selector: str) ->  List[str]:
    return await node.querySelectorAllEval(selector, 'nodes => nodes.map(node => node.innerText.normalize("NFKC"))')


@_catch_missing_elem
async def inner_attribute_all(node: Union[ElementHandle, Page], selector: str, attribute = 'href') ->  List[str]:
    return await node.querySelectorAllEval(selector, f'nodes => nodes.map(node => node.getAttribute("{attribute}"))')


async def hideAutomation(page: Page):
    await page.setUserAgent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.39 Safari/537.36")   
    js_code = pkg_resources.read_text(gscrape.scripts, 'preload.js')
    await page.evaluateOnNewDocument(js_code)

  