# gscrape - google scraper tool

- handles various search elements, e.g. news cards, images, videos, organic results, twitter carousel (see examples)
- gps geolocation can be overridden
- proxy server can be provided
- based on headless chrome and modified [`pyppeteer`](https://github.com/miyakogi/pyppeteer) library

## installation

```shell
pip install git+https://github.com/bonartm/gscrape.git
```

## programmatic usage

```python
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
```

## command line usage

### usage

```shell
usage: gscrape [-h] [--latlng <lat>,<lng>] [--autocomplete] [--url URL]
               [--graphical] [--proxy http://user:password@localhost:port]
               term

Scrape Google's autocomplete and first result page

positional arguments:
  term                  search term

optional arguments:
  -h, --help            show this help message and exit
  --latlng <lat>,<lng>  set geolocation (default: "52.520008,13.404954"
                        (Berlin))
  --autocomplete        retrieve autocompletions
  --url URL             google url (default: "https://www.google.com")
  --graphical           start chrome in graphical mode (default: False)
  --proxy http://user:password@localhost:port
                        proxy server url
```

### example autocompletions

```shell
gscrape --latlng 40.7,-74 --autocomplete 'angela merkel '
```

```json
[
  "angela merkel age\n65 years",
  "angela merkel children",
  "angela merkel shakes",
  "angela merkel harvard",
  "angela merkel net worth",
  "angela merkel biography",
  "angela merkel approval rating",
  "angela merkel successor",
  "angela merkel meme",
  "angela merkel stepping down"
]
```

### example result page

```shell
python -m gscrape.run --latlng 40.7,-74 'angela merkel'
```

```json
[
  {
    "stats": "About 103,000,000 results (0.65 seconds) "
  },
  {
    "appbar": []
  },
  {
    "organic": [
      {
        "url": "https://en.wikipedia.org/wiki/Angela_Merkel",
        "title": "Angela Merkel - Wikipedia",
        "snippet": "Angela Dorothea Merkel (/ˈmɜːrkəl, ˈmɛərkəl/, German: [aŋˈɡeːla doʁoˈteːa ˈmɛʁkl̩]; née Kasner; born 17 July 1954) is a German politician serving as Chancellor of Germany since 2005. She served as the leader of the centre-right Christian Democratic Union (CDU) from 2000 to 2018."
      }
    ]
  },
  {
    "topstories_carousel": [
      {
        "title": "Royal blunder: Confused Angela Merkel in gaffe during chat with Queen - 'Which France?'",
        "url": "https://www.express.co.uk/news/royal/1184869/Angela-Merkel-royal-news-blunder-Queen-Maxima-Netherlands-France-UN-Assembly-latest",
        "source": "Daily Express",
        "time": "1 day ago"
      },
      {
        "title": "Germany: 'No rift' between Chancellor Merkel and likely successor",
        "url": "https://www.dw.com/en/germany-no-rift-between-chancellor-merkel-and-likely-successor/a-50632078",
        "source": "DW",
        "time": "3 days ago"
      },
      ["..."]
    ]
  },
  {
    "peopleasked": [
      "What languages does Angela Merkel speak?",
      "How old is Angela Merkel?",
      "How long can you be chancellor in Germany?",
      "Where was Angela Merkel born?"
    ]
  },
  {
    "videos": [
      {
        "url": "https://www.youtube.com/watch?v=q3-lm7wheD0",
        "title": "Is Angela Merkel a lame duck? | DW News",
        "source": "DW News",
        "platform": "YouTube ",
        "time": " 1 day ago"
      },
      {
        "url": "https://www.youtube.com/watch?v=mT-2zHU9NT8",
        "title": "German Chancellor Angela Merkel's visit to China and trade is ...",
        "source": "CGTN",
        "platform": "YouTube ",
        "time": " Sep 7, 2019"
      },
      ["..."]
    ]
  },
  {
    "organic": [
      {
        "url": "https://www.theguardian.com/world/angela-merkel",
        "title": "Angela Merkel | World | The Guardian",
        "snippet": "7 days ago - Merkel promises €500m to revitalise German forests. Storms ... Hong Kong: Angela Merkel says China must 'guarantee' rights and freedoms."
      },
      {
        "url": "https://www.nytimes.com/topic/person/angela-merkel",
        "title": "Angela Merkel - The New York Times",
        "snippet": "News about Angela Merkel. Commentary and archival information about Angela Merkel from The New York Times."
      },
      {
        "url": "https://www.independent.co.uk/topic/AngelaMerkel",
        "title": "Angela Merkel - latest news, breaking stories and comment ...",
        "snippet": "All the latest breaking news on Angela Merkel. Browse The Independent's complete collection of articles and commentary on Angela Merkel."
      },
      ["..."]
    ]
  },
  {
    "suggestions": [
      "angela merkel education",
      "angela merkel husband",
      "angela merkel children",
      "angela merkel net worth",
      "angela merkel parents",
      "angela merkel age",
      "angela merkel successor",
      "angela merkel twitter"
    ]
  },
  {
    "location": "Brooklyn Heights, Brooklyn, NY"
  }
]
```
