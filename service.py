"""
spyne-flask webservice
prende in input gli url dei wsdl dei negozi e poi li quera uno per volta per ottenere i risultati
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



shops = json.load('shops.json')

app = Flask(__name__)
spyne = Spyne(app)

def get_all_albums():
    for url in shops:
        c = Client(url)
        return c.service.get_all_album()

def get_album(name):
    raise NotImplementedError #TODO
    

@app.route('/cane')
#@app.route('/cane/<query>')
def cane():
    rv = get_albums();
    return render_template('service.html', rv=rv)


@app.route('/album')
def album():
    s = ""
    srv_url = 'http://localhost:8000/?wsdl'
    c = Client(srv_url)
    x = c.service.get_all_album()
    for i in x[0]:
        s += "<p>" + i.title + "</p>"
    return s

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
    #debug andra tolto
    app.debug = True
    #il tutto viene avviato qui: http://localhost:porta/
    app.run(port = 5000)

if __name__ == '__main__':
    app.debug = True
    app.run(port = 5000)