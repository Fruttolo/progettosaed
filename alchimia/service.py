##spyne-flask webservice
#prende in input gli url dei wsdl dei negozi e poi li quera uno per volta per ottenere i risultati
from flask import Flask
from flask import render_template
from flask.ext.spyne import Spyne
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable, ComplexModel

from suds.client import Client

import logging
h = logging.StreamHandler()
rl = logging.getLogger()
rl.setLevel(logging.DEBUG)
rl.addHandler(h)

app = Flask(__name__)
spyne = Spyne(app)

shops = {"negozio1": "http://localhost:8000/?wsdl"}

class RegisterService(spyne.Service):
    __service_url_path__ = '/soap/registrationservice'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()
    """
    this service generates a dictonary of registered shop which shall be queried for results
    """
    @spyne.srpc(Unicode, Unicode, _returns=Integer)
    def register_shop(shop_name, shop_url):
    	shops[shop_name] = shop_url
    	return 1
###########################################
#TODO
"""
a function which connects to each shop in the dict and retrives albums throught their web service
"""
def get_albums():
    srv_url = 'http://localhost:8000/?wsdl'
    c = Client(srv_url)
    return c.service.get_all_album()


#####################
#PRETTY HOMEPAGE PART YAY
######################
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
    app.debug = True
    app.run(port = 5000)