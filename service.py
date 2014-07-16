"""
Modulo che implementa il servizio unificato.
Carica una lista di magazzini e tenta di connettervisi.
Invia una query con i parametri ricevuti dal form di ricerca.
Ottiene un array di oggetti e li mostra al cliente.

"""

from flask import Flask
from flask import render_template
from flask import request
import os
import query

app = Flask(__name__)

@app.route('/index')
def index():
	return render_template('service.html', rv=None)

@app.route('/index', methods=['POST']) 
def search():
	year = request.form['year']
	if year == '':
		year = None
	price = request.form['price']
	if price == '':
		price = None
	rv = query.get_records(title=request.form['title'], author=request.form['author'], year=year, genre=request.form['genre'], price=price)
	return render_template('service.html', rv=rv)

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) #[0] is __name__
    #app.debug = True
    app.run(port=port,debug=True)