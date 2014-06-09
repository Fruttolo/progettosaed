"""Modulo che implementa il servizio unificato.

Carica una lista dei negozi aderenti all'iniziativa,
cerca di connettervisi,
si mette a rispondere alle query.

"""

import logging
h = logging.StreamHandler()
rl = logging.getLogger()
rl.setLevel(logging.DEBUG)
rl.addHandler(h)

import json

from flask import Flask
from flask import render_template

from suds.client import Client

shop_urls = json.load('shops.json')
shops = [Client(url) for url in shop_urls) #TODO: gestire riconnessioni

app = Flask(__name__)

def get_all_records():
    for c in shops:
        return c.service.get_all_records()

@app.route('/cane') #@app.route('/cane/?<query>')
def cane():
    rv = get_all_records();
    return render_template('service.html', rv=rv)

if __name__ == '__main__':
    # db.create_all()
    # admin = User('adminaa', 'adminaa@example.com')
    # guest = User('guestaa', 'guestaa@example.com')
    # # # maligno = Album('Capro', 'Maligno','Sludge')
    # # # badthings = Album('Carcione', 'Bad Things','Blues')
    # db.session.flush()
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.commit()
    app.debug = True
    app.run(port = 5000)