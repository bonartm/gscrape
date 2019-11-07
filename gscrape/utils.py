import importlib.resources as pkg_resources
import logging
from typing import Callable, List, Any, Union
from pyppeteer.element_handle import ElementHandle
from pyppeteer.page import Page
from pyppeteer.errors import ElementHandleError
import gscrape.scripts


def _catch_missing_elem(fun: Callable) -> Callable:
    async def handler(node, selector, *args, **kwargs):
        try:
            return await fun(node, selector, *args, **kwargs)
        except ElementHandleError:
            logging.warning("Element %s does not exist", selector)
            return None
    return handler


def save_list_get(l, idx, default=None):
    try:
        return l[idx]
    except IndexError:
        logging.warning("Index %s does not exist in list %s", idx, l)
        return default


def to_dict(**kwargs: List[Any]):
    """parses lists to flattened list of dictionaries"""
    n = len(next(iter(kwargs.values())))
    res = []
    for i in range(n):
        res.append({
            key: save_list_get(value, i) for key, value in kwargs.items()
        })
    return res


@_catch_missing_elem
async def inner_text(node: Union[ElementHandle, Page], selector: str) -> str:
    """returns inner text of a html node"""
    return await node.querySelectorEval(selector, 'node => node.innerText.normalize("NFKC")')


@_catch_missing_elem
async def inner_attribute(node: Union[ElementHandle, Page],
                          selector: str, attribute='href') -> str:
    """returns inner attribute of a html node"""
    return await node.querySelectorEval(selector, f'node => node.getAttribute("{attribute}")')


@_catch_missing_elem
async def inner_text_all(node: Union[ElementHandle, Page],
                         selector: str) -> List[str]:
    """returns list of inner text from list of nodes"""
    return await node.querySelectorAllEval(
        selector,
        'nodes => nodes.map(node => node.innerText.normalize("NFKC"))'
    )


@_catch_missing_elem
async def inner_attribute_all(
        node: Union[ElementHandle, Page],
        selector: str, attribute='href') -> List[str]:
    """returns list of inner attributes from list of nodes"""
    return await node.querySelectorAllEval(
        selector,
        f'nodes => nodes.map(node => node.getAttribute("{attribute}"))'
    )


async def hideAutomation(page: Page):
    """adds various javascript methods to hide automation from websites"""
    js_code = pkg_resources.read_text(gscrape.scripts, 'preload.js')
    await page.evaluateOnNewDocument(js_code)
