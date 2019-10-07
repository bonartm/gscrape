from gscrape.interface import SearchInterface
from gscrape.serp import GoogleSerp
import asyncio
import pytest
import os
import json



pytestmark = pytest.mark.asyncio

@pytest.yield_fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope='session')
async def serp():
    with open("./gscrape/structure.json") as f:
        structure = json.load(f)
    
    path = os.path.dirname(__file__)
    url = f"file:///{path}/test1.html"
    lat, lng = (52.34, 23.459)
    interface = SearchInterface(url, lat, lng, False)
    await interface.launch()
    context = await interface.browser.createIncognitoBrowserContext()
    page = await context.newPage()
    await page.goto(url)  
    serp = GoogleSerp(page, structure)
    await serp.scrape()
    await interface.browser.close()
    return serp

async def test_serp(serp):
    with open("out.json", "w") as f:
        json.dump(serp.serp, f, indent = 2)
    assert True


    


# async def test_elem(serp):    
#     assert  serp.get_keys() == [
#         se.STATS, 
#         se.APPBAR,
#         se.TOPSTORIES_CAROUSEL,
#         se.ORGANIC,
#         se.IMAGES,
#         se.ORGANIC,
#         se.VIDEOS,
#         se.ORGANIC,
#         se.PEOPLEASKED,
#         se.ORGANIC,
#         se.SUGGESTIONS,
#         se.LOCATION]

# async def test_stats(serp):
#     assert serp.get(se.STATS) == "Ungefähr 98.200.000 Ergebnisse (0,51 Sekunden) "

# async def test_appbar(serp):    
#     assert serp.get(se.APPBAR) == []

# async def test_topstories(serp):    
#     assert len(serp.get(se.TOPSTORIES_CAROUSEL)) == 10













  
       
        