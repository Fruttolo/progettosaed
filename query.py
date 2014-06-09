import json

from suds.client import Client

shop_urls = json.load('shops.json')
shop_clients = [Client(url) for url in shop_urls) #TODO: gestire riconnessioni