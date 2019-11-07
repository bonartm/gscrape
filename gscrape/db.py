from pymongo import MongoClient
import datetime


class GoogleMongo:

    def __init__(self, uri: str):
        self.client = MongoClient(uri)
        self.db = self.client['gscrape']

    def save_serp(self, queryterm, proxy, lat, lon, graphical, serp):
        self.db['test'].insert_one({
            'date': datetime.datetime.utcnow(),
            'queryterm': queryterm,
            'proxy': proxy.hostname,
            'latlon': [lat, lon],
            'headless': not graphical,
            'stats': serp['stats'],
            'appbar': serp['appbar'],
            'suggestions': serp['suggestions'],
            'google_location': serp['location'],
            'elements': serp['elements']
        })
