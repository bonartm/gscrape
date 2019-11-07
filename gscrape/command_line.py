import asyncio
import argparse
import json
from gscrape.interface import SearchInterface


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


def _parse_geo(str: str):
    latlon = str.split(',', maxsplit=2)
    return (float(el) for el in latlon)


async def _run(args):
    lat, lon = None, None
    if args.latlon is not None:
        lat, lon = _parse_geo(args.latlon)
    async with SearchInterface(args.url, lat, lon, args.graphical, args.proxy, args.mongodb) as interface:
        if args.autocomplete:
            completions = await interface.autocomplete(args.term)
            print(json.dumps(completions, indent=2, ensure_ascii=False))
        else:
            serp = await interface.serp(args.term)
            print(json.dumps(serp, indent=2, ensure_ascii=False))


def main():
    """main entry point for command line usage"""
    parser = argparse.ArgumentParser(
        description="Scrape Google's autocomplete and first result page")
    parser.add_argument('term', type=str, help='search term')
    parser.add_argument('--latlon',
                        help='set geolocation (default: None)',
                        metavar='<lat>,<lon>', default=None)
    parser.add_argument('--url',
                        help='google url (default: "https://www.google.com")',
                        default='https://www.google.com', metavar='<url>')
    parser.add_argument('--proxy',
                        help='proxy server url (default: None)',
                        metavar='http://user:password@host:port', default=None)
    parser.add_argument('--graphical',
                        help='start chrome in graphical mode',
                        action='store_true', default=False)
    parser.add_argument('--autocomplete',
                        action='store_true',
                        help='retrieve autocompletions')
    parser.add_argument('--mongodb',
                        help='save SERP in mongodb instance (default: None)',
                        metavar='mongodb://username:password@host/database',
                        default=None)
    args = parser.parse_args()
    asyncio.run(_run(args))


if __name__ == "__main__":
    main()
