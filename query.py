import json

from suds.client import Client

urls = json.load(open('shops.json', 'r'))
#TODO: gestire riconnessioni
#clients = [Client(url) for url in shop_urls]
clients = [Client("http://127.0.0.1:8000?wsdl")]
clients[0].factory.create("ns1:Record")
def query(title=None, author=None, genre=None, year=None, thumbnail_url=None, description=None, quantity=None):
    for c in clients:
        rq = c.factory.create("ns1:Record") #HACK MA STO SMADONNANDO
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