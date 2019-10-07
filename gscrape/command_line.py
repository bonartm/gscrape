import asyncio
import json
from gscrape.interface import SearchInterface
import argparse

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

async def run(args): 
    lat, lng = None, None 
    if args.latlng is not None:
        lat, lng = parse_geo(args.latlng)
    interface = SearchInterface(args.url, lat, lng, args.graphical, args.proxy)
    await interface.launch()
    if(args.autocomplete):
        completions = await interface.autocomplete(args.term)
        print(json.dumps(completions, indent = 2, ensure_ascii=False))
    else:    
        serp = await interface.serp(args.term)
        print(json.dumps(serp, indent = 2, ensure_ascii=False))
    await interface.browser.close()


def main():
    parser = argparse.ArgumentParser(description="Scrape Google's autocomplete and first result page")
    parser.add_argument('term', type=str, help='search term')
    parser.add_argument('--latlng', help = 'set geolocation (default: None)', metavar='<lat>,<lng>', default = None)
    parser.add_argument('--url', help = 'google url (default: "https://www.google.com")', default = 'https://www.google.com', metavar='<url>')
    parser.add_argument('--proxy', help = 'proxy server url (default: None)', metavar = 'http://user:password@localhost:port', default=None)
    parser.add_argument('--graphical', help = 'start chrome in graphical mode', action='store_true', default=False)
    parser.add_argument('--autocomplete', action='store_true', help = 'retrieve autocompletions')

    args = parser.parse_args()

    asyncio.get_event_loop().run_until_complete(run(args))



if __name__ == "__main__": 
    main()