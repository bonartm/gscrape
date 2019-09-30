import asyncio
from pyppeteer import launch
from pprint import pprint
import json
from gscrape.interface import SearchInterface
import argparse
import gscrape.patches

# Paris:[48.857317, 2.317781]
# London:[51.496773, -0.119009]
# NewYork:[40.738487, -73.982401]
# LosAngeles:[34.050077, -118.209594]
# Cologne:[50.935612, 6.927694]
# Berlin:[52.512276, 13.410570]
# Moskow:[55.739966, 37.617767]
# Frankfurt:[50.102612, 8.691650]
# Rome:[41.902198, 12.473667]
# Oslo:[59.911491, 10.757933]
# Detroit: [42.333203, -83.050949]


def parse_geo(str: str):
    latlng = str.split(',', maxsplit=2)
    return (float(el) for el in latlng)


async def main(args):
    gscrape.patches.disable_timeout()
    gscrape.patches.add_geolocation()
    gscrape.patches.add_permissions()
    lat, lng = parse_geo(args.latlng)

    chrome_args = [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-infobars',
        '--window-position=0,0',
        '--ignore-certifcate-errors',
        '--ignore-certifcate-errors-spki-list',
        '--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3312.0 Safari/537.36"'
    ]

    browser = await launch({'headless':not args.graphical, 'slowMo': 20 if args.graphical else 0}, args=chrome_args)
    interface = SearchInterface(browser, args.url, lat, lng)
    if(args.autocomplete):
        completions = await interface.autocomplete(args.term)
        print(json.dumps(completions, indent = 2, ensure_ascii=False))
    else:    
        serp = await interface.serp(args.term)
        print(json.dumps(await serp.scrape(), indent = 2, ensure_ascii=False))
    await browser.close()
    

parser = argparse.ArgumentParser(description="Scrape Google's autocomplete and first result page")
parser.add_argument('term', type=str, help='search term')
parser.add_argument('--latlng', help = 'set geolocation (default: "52.520008,13.404954" (Berlin))', metavar='<lat>,<lng>', default = '52.520008,13.404954')
parser.add_argument('--autocomplete', action='store_true', help = 'retrieve autocompletions')
parser.add_argument('--url', help = 'google url (default: "https://www.google.com")', default = 'https://www.google.com')
parser.add_argument('--graphical', help = 'start chrome in graphical mode (default: False)', action='store_true', default=False)
args = parser.parse_args()

asyncio.get_event_loop().run_until_complete(main(args))