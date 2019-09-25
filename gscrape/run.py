import asyncio
from pyppeteer import launch
from pprint import pprint
import json
from gscrape.interface import SearchInterface
import argparse

def patch_pyppeteer():
    import pyppeteer.connection
    original_method = pyppeteer.connection.websockets.client.connect
    def new_method(*args, **kwargs):
        kwargs['ping_interval'] = None
        kwargs['ping_timeout'] = None
        return original_method(*args, **kwargs)
    pyppeteer.connection.websockets.client.connect = new_method


async def main(args):
    patch_pyppeteer()
    browser = await launch({'headless':True})
    interface = SearchInterface(browser, args.url)
    if(args.autocomplete):
        completions = await interface.autocomplete(args.term)
        print(json.dumps(completions, indent = 2, ensure_ascii=False))
    else:    
        serp = await interface.serp(args.term)
        print(json.dumps(await serp.scrape(), indent = 2, ensure_ascii=False))
    await browser.close()
    

parser = argparse.ArgumentParser(description="Scrape Google's autocomplete and first result page")
parser.add_argument('term', type=str, help='search term')
parser.add_argument('--autocomplete', action='store_true', help = 'retrieve autocompletions')
parser.add_argument('--url', help = 'google url (default: "https://www.google.de")',
    default = "https://www.google.de")
args = parser.parse_args()
asyncio.get_event_loop().run_until_complete(main(args))