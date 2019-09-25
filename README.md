# gscrape - yet another google scraper tool

- handles various search elements, e.g. news cards, images, videos, organic results (see examples)
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
python -m gscrape.run --autocomplete 'angela merkel '
```

```json
[
  "angela merkel zittern",
  "angela merkel alter",
  "angela merkel kinder",
  "angela merkel krank",
  "angela merkel trennung",
  "angela merkel ehemann",
  "angela merkel zitteranfall",
  "angela merkel gehalt",
  "angela merkel urlaub",
  "angela merkel mann"
]
```

### result page

```shell
python -m gscrape.run 'angela merkel' > out.json
```

```json
[
  {
    "stats": "Ungefähr 111.000.000 Ergebnisse (0,51 Sekunden) "
  },
  {
    "topstories_carousel": [
      {
        "title": "Merkel gegen Greta – erstmals übt die Kanzlerin Kritik an der Klimaschützerin",
        "url": "https://www.welt.de/politik/ausland/plus200899182/Merkel-gegen-Greta-erstmals-uebt-die-Kanzlerin-Kritik-an-der-Klimaschuetzerin.html",
        "source": "Die Welt",
        "time": "vor 4 Stunden"
      },
      {
        "title": "„Sie ist krank“: Angela Merkel und Friedrich Merz kritisieren Greta Thunberg",
        "url": "https://www.ksta.de/politik/-sie-ist-krank--merz-kritisiert-thunbergs-eltern---merkel-widerspricht-der-schwedin-33219826",
        "source": "Kölner Stadt-Anzeiger",
        "time": "vor 5 Stunden"
      },
      {
        "title": "Am Tisch mit Irans Präsident Rouhani - Warum traf Merkel diesen Ober-Mullah?",
        "url": "https://www.bild.de/politik/ausland/politik-ausland/am-tisch-mit-irans-praesident-rouhani-warum-traf-merkel-diesen-ober-mullah-64936354.bild.html",
        "source": "Bild.de",
        "time": "vor 24 Minuten"
      }
    ]
  },
  {
    "organic": [
      {
        "url": "https://www.angela-merkel.de/",
        "title": "Angela Merkel",
        "snippets": "Wir verwenden auf dieser Website notwendige Cookies. Durch Nutzung unserer Webseite stimmen Sie zu, dass Cookies gesetzt werden. Außerdem verwenden ..."
      },
      {
        "url": "https://de.wikipedia.org/wiki/Angela_Merkel",
        "title": "Angela Merkel – Wikipedia",
        "snippets": "Angela Dorothea Merkel (* 17. Juli 1954 in Hamburg als Angela Dorothea Kasner) ist eine deutsche Politikerin (CDU). Sie ist seit dem 22. November 2005 ..."
      }
    ]
  },
  {
    "videos": [
      {
        "url": "https://www.bild.de/video/clip/greta-thunberg/kanzlerin-merkel-widerspricht-greta-agvideo-64925586.bild.html",
        "title": "Angela Merkel widerspricht Greta Thunberg nach ihrer Wutrede",
        "source": "",
        "time": " vor 8 Stunden",
        "platform": "Bild.de "
      },
      {
        "url": "https://www.youtube.com/watch?v=i0YmTKL-zrY",
        "title": "UN-Klimagipfel: Rede von Bundeskanzlerin Angela Merkel ...",
        "source": "phoenix",
        "time": " vor 2 Tagen",
        "platform": "YouTube "
      },
      {
        "url": "https://www.bild.de/video/clip/klimawandel/merkel-rede-beim-un-klima-gipfel-reuters-64893900.bild.html",
        "title": "Klimawandel: Angela Merkel beim UN-Klimagipfel in New York",
        "source": "",
        "time": " vor 2 Tagen",
        "platform": "Bild.de "
      },
      {
        "url": "https://www.bild.de/video/clip/angela-merkel/merkel-man-muss-den-wissenschaftlichen-beweisen-folgen-agvideo-64836918.bild.html",
        "title": "Angela Merkel | Man muss den wissenschaftlichen Beweisen ...",
        "source": "",
        "time": " vor 5 Tagen",
        "platform": "Bild.de "
      },
      {
        "url": "https://www.youtube.com/watch?v=nj0UWDWlcSc",
        "title": "Nach Thunbergs Wutrede: Kanzlerin Merkel widerspricht Greta",
        "source": "BILD",
        "time": " vor 6 Stunden",
        "platform": "YouTube "
      },
      {
        "url": "https://www.bild.de/video/clip/klimaschutz/diskussion-um-langstreckenfluege-der-bundesregierung-agvideo-64873224.bild.html",
        "title": "Angela Merkel und Annegret Kramp-Karrenbauer fliegen ...",
        "source": "",
        "time": " vor 3 Tagen",
        "platform": "Bild.de "
      },
      {
        "url": "https://www.prosieben.de/tv/galileo/videos/234-treffen-mit-donald-trump-was-hat-angela-merkel-hier-wohl-gedacht-clip",
        "title": "Treffen mit Donald Trump: Was hat Angela Merkel hier wohl gedacht?",
        "source": "",
        "time": " 30.08.2019",
        "platform": "ProSieben "
      },
      {
        "url": "https://www.bundeskanzlerin.de/bkin-de/mediathek/videos",
        "title": "Videos",
        "source": "",
        "time": " vor 2 Tagen",
        "platform": "Bundeskanzlerin | Videos "
      },
      {
        "url": "https://www.daserste.de/unterhaltung/quiz-show/hirschhausens-quiz-des-menschen/videos/deepfake-hqdm-xxl-5-100.html",
        "title": "Video: Deepfake: Angela Merkel - Hirschhausens Quiz des Menschen - ARD",
        "source": "",
        "time": " vor 4 Tagen",
        "platform": "DasErste.de "
      },
      {
        "url": "https://www.bild.de/video/clip/angela-merkel/angela-merkel-zittert-bei-empfang-vor-kanzleramt-62709658.bild.html",
        "title": "Angela Merkel zittert bei Nationalhymne - Sorge um unsere ...",
        "source": "",
        "time": " 18.06.2019",
        "platform": "Bild.de "
      }
    ]
  },
  {
    "peopleasked": [
      "Wo wohnt Angela Merkel?",
      "Was hat Angela Merkel studiert?",
      "Wo hat Angela Merkel studiert?",
      "Wer war der längste Bundeskanzler?"
    ]
  },
  {
    "images": [
      {
        "url": "https://www.spiegel.de/politik/ausland/usa-angela-merkel-weist-iran-forderungen-nach-ende-der-sanktionen-zurueck-a-1288460.html",
        "imgsrc": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/"
      },
      {
        "url": "https://de.wikipedia.org/wiki/Angela_Merkel",
        "imgsrc": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/"
      },
      {
        "url": "https://www.spiegel.de/video/angela-merkel-beim-uno-klimagipfel-video-99029880.html",
        "imgsrc": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/"
      },
      {
        "url": "https://www.horizont.net/marketing/nachrichten/getrennte-fluege-sixt-arbeitet-sich-jetzt-auch-an-angela-merkel-und-akk-ab-177787",
        "imgsrc": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/"
      },
      {
        "url": "https://www.zeit.de/politik/ausland/2019-09/un-generalversammlung-angela-merkal-donald-trump-hassan-rohani-treffen",
        "imgsrc": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
      },
      {
        "url": "https://www.spiegel.de/politik/ausland/angela-merkel-beim-uno-klimagipfel-in-new-york-weltenretterin-a-d-a-1288233.html",
        "imgsrc": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
      },
      {
        "url": "https://www.youtube.com/watch?v=i0YmTKL-zrY",
        "imgsrc": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
      },
      {
        "url": "https://www.cdu.de/vorstand/dr-angela-merkel",
        "imgsrc": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
      },
      {
        "url": "https://www.zeit.de/politik/ausland/2019-09/angela-merkel-usa-iran-donald-trump-un",
        "imgsrc": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
      },
      {
        "url": "https://www.focus.de/politik/ausland/nach-un-klima-gipfel-in-new-york-kanzlerin-lobt-greta-fuer-aufruettelnde-rede-doch-in-einem-punkt-widerspricht-sie_id_11180495.html",
        "imgsrc": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
      }
    ]
  },
  {
    "organic": [
      {
        "url": "https://www.welt.de/politik/ausland/plus200899182/Merkel-gegen-Greta-erstmals-uebt-die-Kanzlerin-Kritik-an-der-Klimaschuetzerin.html",
        "title": "Merkel gegen Greta – erstmals übt die Kanzlerin Kritik an der ...",
        "snippets": "vor 5 Stunden - Zaghaft, fast schüchtern war die Kritik, die Angela Merkel an Greta Thunberg richtete. Kurz vor ihrem Abflug vom UN-Klimagipfel in New York ..."
      },
      {
        "url": "https://www.bundeskanzlerin.de/bkin-de/angela-merkel",
        "title": "Angela Merkel - Bundeskanzlerin",
        "snippets": "Terminkalender. Ob Staatsbesuch, Regierungserklärung oder Video-Podcast: Hier erhalten Sie einen Überblick über die öffentlichen Termine der ..."
      },
      {
        "url": "https://www.n-tv.de/politik/Angela-Merkel-eilt-von-Krise-zu-Krise-article21294265.html",
        "title": "Potpourri in New York: Angela Merkel eilt von Krise zu Krise ...",
        "snippets": "vor 7 Stunden - Bundeskanzlerin Angela Merkel hat ihre Reise wie immer vollgestopft mit einer Fülle von Themen und Terminen: Klimarettung, Iran-Abkommen ..."
      },
      {
        "url": "https://www.hdg.de/lemo/biografie/angela-merkel.html",
        "title": "LeMO Biografie Angela Merkel",
        "snippets": "Angela Merkel ist eine deutsche CDU-Politikerin und seit 2005 als erste Frau Bundeskanzlerin der Bundesrepublik Deutschland."
      },
      {
        "url": "https://www.spiegel.de/politik/deutschland/angela-merkel-in-new-york-die-diplomatin-a-1288480.html",
        "title": "Angela Merkel in New York: Die Diplomatin - SPIEGEL ONLINE",
        "snippets": "vor 9 Stunden - Am Ende dieses zweiten Tages bei den Vereinten Nationen kümmert sich Angela Merkel wieder um die großen Konflikte dieser Welt, vor allem ..."
      }
    ]
  },
  {
    "suggestions": [
      "angela merkel lebenslauf",
      "angela merkel kinder",
      "angela merkel mann",
      "angela merkel jung",
      "angela merkel trennung",
      "angela merkel gehalt",
      "angela merkel wohnung",
      "angela merkel wiki"
    ],
    "location": "53115, Bonn"
  }
]
```
