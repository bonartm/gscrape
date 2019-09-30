# gscrape - yet another google scraper tool

- handles various search elements, e.g. news cards, images, videos, organic results, twitter carousel (see examples)
- uses headless chrome and the [`pyppeteer`](https://github.com/miyakogi/pyppeteer) library
- unstable version under heavy development

## requirements

```shell
conda create --name gscrape --file requirements.txt
conda activate gscrape
```

## examples

### autocompletions

```shell
python -m gscrape.run --latlng 40.7,-74 --autocomplete 'angela merkel '
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

### result page

```shell
python -m gscrape.run --latlng 40.7,-74 'angela merkel'
```

```json
[
  {
    "stats": "About 106,000,000 results (0.70 seconds) ",
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
        "title": "Merkel crisis: Chancellor’s conservatives LOSE support as SPD allies gain - poll",
        "url": "https://www.express.co.uk/news/world/1184244/angela-merkel-news-germany-CDU-SPD-merkel-health-latest",
        "source": "Daily Express",
        "time": "14 hours ago"
      },
      {
        "title": "Germany: 'No rift' between Chancellor Merkel and likely successor",
        "url": "https://www.dw.com/en/germany-no-rift-between-chancellor-merkel-and-likely-successor/a-50632078",
        "source": "DW",
        "time": "1 day ago"
      },
      {
        "title": "From Merkel to Adenauer, biting caricatures of Germany's chancellors",
        "url": "https://www.dw.com/en/from-merkel-to-adenauer-biting-caricatures-of-germanys-chancellors/g-50589356",
        "source": "DW",
        "time": "6 hours ago"
      },
      {
        "title": "Merkel's conservatives vow to stick to policy of no new debt",
        "url": "https://www.reuters.com/article/us-germany-debt-cdu/merkels-conservatives-vow-to-stick-to-policy-of-no-new-debt-idUSKBN1WF0QG",
        "source": "Reuters",
        "time": "7 hours ago"
      },
      {
        "title": "Germany Offended By Ukrainian President's Comments over Angela Merkel in Call to Donald Trump- Report",
        "url": "https://sputniknews.com/europe/201909291076916847-germany-offended-zelensky-trump-call/",
        "source": "Sputnik International",
        "time": "1 day ago"
      },
      {
        "title": "Merkel's conservatives lose support, SPD allies gain: poll",
        "url": "https://news.yahoo.com/merkels-conservatives-lose-support-spd-105907792.html",
        "source": "Yahoo News",
        "time": "1 day ago"
      },
      {
        "title": "Angela Merkel hails Germany's progress since fall of Berlin Wall",
        "url": "https://www.dw.com/en/angela-merkel-hails-germanys-progress-since-fall-of-berlin-wall/a-50620492",
        "source": "DW",
        "time": "2 days ago"
      },
      {
        "title": "France demands Germany up its game - ‘Don’t wait until economic situation worsens!’",
        "url": "https://www.express.co.uk/news/world/1183653/eu-news-eurozone-crisis-france-germany-angela-merkel",
        "source": "Daily Express",
        "time": "2 days ago"
      },
      {
        "title": "Macron and Merkel's ultimatum to Boris: PM given just one week to prevent Brexit delay",
        "url": "https://www.express.co.uk/news/uk/1183611/Brexit-news-UK-EU-Boris-Johnson-Ireland-backstop-stephen-barclay-no-deal-macron-merkel",
        "source": "Daily Express",
        "time": "2 days ago"
      },
      {
        "title": "Merkel and Macron savaged by Trump lawyer over Iran dealings: 'Giving money to terrorists!",
        "url": "https://www.express.co.uk/news/world/1183508/eu-news-merkel-macron-trump-giuliani-iran-terrorists-money-spt",
        "source": "Daily Express",
        "time": "3 days ago"
      }
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
    "organic": [
      {
        "url": "https://www.theguardian.com/world/angela-merkel",
        "title": "Angela Merkel | World | The Guardian",
        "snippet": "5 days ago - Merkel promises €500m to revitalise German forests. Storms ... Hong Kong: Angela Merkel says China must 'guarantee' rights and freedoms."
      },
      {
        "url": "https://www.nytimes.com/topic/person/angela-merkel",
        "title": "Angela Merkel - The New York Times",
        "snippet": "News about Angela Merkel. Commentary and archival information about Angela Merkel from The New York Times."
      }
    ]
  },
  {
    "videos": [
      {
        "url": "https://www.youtube.com/watch?v=mT-2zHU9NT8",
        "title": "German Chancellor Angela Merkel's visit to China and trade is ...",
        "source": "CGTN",
        "platform": "YouTube ",
        "time": " Sep 7, 2019"
      },
      {
        "url": "https://www.youtube.com/watch?v=VuzpVJ5z56k",
        "title": "Angela Merkel: Violence must be avoided, dialogue the best ...",
        "source": "CGTN",
        "platform": "YouTube ",
        "time": " Sep 6, 2019"
      },
      {
        "url": "https://www.youtube.com/watch?v=OR7Ug5y-va8",
        "title": "Angela Merkel seen shaking for a third time - BBC News",
        "source": "BBC News",
        "platform": "YouTube ",
        "time": " Jul 11, 2019"
      },
      {
        "url": "https://www.cnn.com/videos/world/2019/06/27/germany-angela-merkel-shaking-lon-orig-ge.cnn",
        "title": "Angela Merkel seen shaking for third time in under a month",
        "source": "",
        "platform": "CNN.com ",
        "time": " Jun 27, 2019"
      },
      {
        "url": "https://www.youtube.com/watch?v=vfWf8N8wx0Y",
        "title": "Angela Merkel insists she is 'fine' after third bout of shaking in ...",
        "source": "Guardian News",
        "platform": "YouTube ",
        "time": " Jul 10, 2019"
      },
      {
        "url": "https://www.youtube.com/watch?v=UcTKuB5pQmU",
        "title": "German Chancellor Angela Merkel seen shaking for third time ...",
        "source": "euronews (in English)",
        "platform": "YouTube ",
        "time": " Jul 10, 2019"
      },
      {
        "url": "https://www.youtube.com/watch?v=q7Eb4KVw4nE",
        "title": "What Angela Merkel's exit means for Germany — and Europe",
        "source": "Vox",
        "platform": "YouTube ",
        "time": " Jan 25, 2019"
      },
      {
        "url": "https://www.youtube.com/watch?v=URUqqNdGXNo",
        "title": "Angela Merkel shakes during national anthem, blaming ...",
        "source": "Guardian News",
        "platform": "YouTube ",
        "time": " Jun 18, 2019"
      },
      {
        "url": "https://www.youtube.com/watch?v=mhWkHvayHzo",
        "title": "Live | Angela Merkel and Boris Johnson speak to reporters ...",
        "source": "euronews (in English)",
        "platform": "YouTube ",
        "time": " Aug 21, 2019"
      },
      {
        "url": "https://www.youtube.com/watch?v=5uz7gvwxIso",
        "title": "Angela Merkel challenges Boris Johnson to find backstop ...",
        "source": "Guardian News",
        "platform": "YouTube ",
        "time": " Aug 21, 2019"
      }
    ]
  },
  {
    "organic": [
      {
        "url": "https://www.independent.co.uk/topic/AngelaMerkel",
        "title": "Angela Merkel - latest news, breaking stories and comment ...",
        "snippet": "All the latest breaking news on Angela Merkel. Browse The Independent's complete collection of articles and commentary on Angela Merkel."
      },
      {
        "url": "https://www.forbes.com/profile/angela-merkel/",
        "title": "Angela Merkel - Forbes",
        "snippet": "Merkel became the first female Chancellor of Germany in 2005 and is serving her fourth term. In November Merkel stepped down as leader of the Christian ..."
      },
      {
        "url": "https://www.dw.com/en/germany-no-rift-between-chancellor-merkel-and-likely-successor/a-50632078",
        "title": "Germany: ′No rift′ between Chancellor Merkel and likely ...",
        "snippet": "1 day ago - German Defense Minister Annegret Kramp-Karrenbauer on Sunday denied falling out with Chancellor Angela Merkel after the pair traveled on ..."
      },
      {
        "url": "https://www.britannica.com/biography/Angela-Merkel",
        "title": "Angela Merkel | Biography, Political Career, & Facts ...",
        "snippet": "Aug 21, 2019 - Biography of German politician Angela Merkel, who in 2005 became the first female chancellor of Germany. Her willingness to adopt the ..."
      },
      {
        "url": "https://www.bundeskanzlerin.de/bkin-en/angela-merkel/biography",
        "title": "Bundeskanzlerin | Biography",
        "snippet": "Angela Merkel was sworn in as Chancellor on November 22, 2005. She is the first woman and the first East German to hold this office. Her CV traces the most ..."
      }
    ]
  },
  {
    "suggestions": [
      "angela merkel education",
      "angela merkel husband",
      "angela merkel children",
      "angela merkel net worth",
      "angela merkel parents",
      "angela merkel twitter",
      "angela merkel successor",
      "angela merkel shakes"
    ],
    "location": "Brooklyn Heights, Brooklyn, NY"
  }
]
```
