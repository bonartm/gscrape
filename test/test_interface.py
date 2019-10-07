from gscrape.interface import SearchInterface
import asyncio

url = 'https://www.google.com'
lat = 54.34
lng = 34.2
graphical = False
proxy = None
queryterm = "Donald Trump"

async def scrape():
    interface = SearchInterface(url, lat, lng, graphical, proxy)
    await interface.launch()
    completions = await interface.autocomplete(queryterm)
    serp = await interface.serp(queryterm)
    return (completions, serp)

completions, serp = asyncio.get_event_loop().run_until_complete(scrape())
