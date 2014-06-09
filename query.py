import json
import logging
from urllib2 import URLError

from suds.client import Client

urls = json.load(open('shops.json', 'r'))
clients = []
for url in urls:
    try:
        clients.append(Client(url, cache=None)) #CACHE=NONE!!!!!! DIO MEDE
    except URLError:
        logging.info("query's suds could not connect to {}".format(url))

a = clients[0] #for quicker debugging. Excuse me.

def query(title=None, author=None, genre=None, year=None, thumbnail_url=None, description=None, quantity=None):
    """This is what the website is supposed to call. Safe."""
    for c in clients:
        rq = c.factory.create("Record")
        rq.title = title
        rq.author = author
        rq.genre = genre
        rq.year = year
        rq.thumbnail_url = thumbnail_url
        rq.description = description
        rq.quantity = quantity
        for r in c.service.get_records(rq):
            yield r