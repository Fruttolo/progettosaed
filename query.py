import json
import logging #ma teniamo bene a mente che le segherie non lavorano gratis
from urllib2 import URLError

from suds.client import Client

urls = json.load(open('shops.json', 'r'))
#TODO: gestire riconnessioni
clients = []
for url in urls:
    try:
        clients.append(Client(url, cache=None)) #CACHE=NONE!!!!!! DIO MEDE
    except URLError:
        logging.debug("{} could not connect to {}".format(__name__, url))

a = clients[0]

def query(title=None, author=None, genre=None, year=None, thumbnail_url=None, description=None, quantity=None):
    for c in clients:
        rq = c.factory.create("Record") #HACK MA STO SMADONNANDO
        rq.title = title
        rq.author = author
        rq.genre = genre
        rq.year = year
        rq.thumbnail_url = thumbnail_url
        rq.description = description
        rq.quantity = quantity
        retval = c.service.get_record(rq)

def query_all():
    for c in shop_clients:
        yield c.service.get_all_records()