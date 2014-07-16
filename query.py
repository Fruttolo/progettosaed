"""
Questo modulo è sostanzialmente un client SOAP con cui si interfaccia il servizio principale.
Ottiene i wsdl dei magazzini leggendo il file warehouse.json,
prende in input i parametri della query e restituisce la lista dei risultati della query.
"""
import json
import logging
from urllib2 import URLError

from suds.client import Client

urls = json.load(open('warehouse.json', 'r'))
clients = []
for url in urls:
    try:
        clients.append(Client(url, cache=None))
    except URLError:
        logging.info("query's suds could not connect to {}".format(url))

def get_records(title=None, author=None, genre=None, year=None, thumbnail_url=None, description=None, quantity=None, price = None):
    for c in clients:
        rq = c.factory.create("Record")
        rq.title = title
        rq.author = author
        rq.genre = genre
        rq.year = year
        rq.thumbnail_url = thumbnail_url
        rq.description = description
        rq.quantity = quantity
        rq.price = price
        for r in c.service.get_records(rq):
            yield r
