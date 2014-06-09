import json

from suds.client import Client

shop_urls = json.load('shops.json')
#TODO: gestire riconnessioni
shop_clients = [Client(url) for url in shop_urls)

def query():
    for c in shop_clients:
        rq = c.factory.create("Record")
        rq.title = 'cock'
        retval = c.service.get_record(rq)

def query_all():
    for c in shop_clients:
        yield c.service.get_all_records()