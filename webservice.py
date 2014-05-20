from flask import Flask
#Flask-Enterprise extension for SOAP
from flaskext.enterprise import Enterprise
#Test function
from time import ctime
#SQLite interfacing
import sqlite3
from flask import g

app = Flask(__name__)
enterprise = Enterprise(app)

STRING = enterprise._sp.String

##################
#DATABASE 
#funzioni di gestione del database, copiate pari pari dalla documentazione
##################
home_db = ./index.db
database = []

def get_db(DATABASE):
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()
def create_table(name):
	query = 'CREATE TABLE ' + name + '(Autore char[50],Titolo char[50],Etichetta char[50], Codice[10],Tipo[10])'
	query_db(query,home_db)
		
def register_shop(URL,DB,SHOPNAME):
	create_table(SHOPNAME)
	WSDL = URL + '?wsdl'
	client = Client(url = WSDL, location = URL)
	client.options.cache.clear()
	
	
	
def query_db(query,db, args=(), one=False):
	with app.app_context():
		cur = get_db(db).execute(query, args)
		rv = cur.fetchall()
		cur.close()
		#l'if e levabile e serve per ritornare un solo risultato
		return (rv[0] if rv else None) if one else rv

#flask-enterprise forse passa anche gli oggetti ma usiamo le strighe :v
def queryToString(query_result):
	with app.app_context():
		string = ""
		for element in query_result:
			for i in element:
				string += i + " "
			string += "\n"
		return string
		
##################
#WEBSERVICE
#la classe che rappresenta il webservice, ogni metodo ha il decoratore con tipi
#di parametri e return
##################
class DemoService(enterprise.SOAPService):
	
	@enterprise.soap(STRING,STRING,STRING, _returns=STRING)
	def register_shop(self, url,db,shopname):
		register(url,db,shopname)
		return "done"
		
#############
#WEBSITE
#qui ci sono le app di flask, ho fatto delle provette poi bisognera fare un frontend carino
#############		
@app.route('/hello')
def hello():
	rs = ""
	for user in query_db('select * from catalogo'):
		 rs+="<p>"
		 for i in user:
		 	rs += i + " "
		 rs+="</p>"
	return rs
#############

if __name__ == '__main__':
	#debug andra tolto
	app.debug = True
	#il tutto viene avviato qui: http://localhost:porta/
	app.run(port = 5001)
