"""Modulo che implementa il servizio unificato.

Carica una lista dei negozi aderenti all'iniziativa,
cerca di connettervisi,
si mette a rispondere alle query.

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
	#if bruttissimo ma altrimenti c'e un conflitto tra tipi in caso di form lasciato vuoto
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