from flask import Flask
<<<<<<< HEAD
from flask import Flask
#Flask-Enterprise extension for SOAP
from flaskext.enterprise import Enterprise
=======
#Flask-Enterprise extension for SOAP
from flask.ext.enterprise import Enterprise
>>>>>>> 2e6ff0a43b69e6b4f84032b7c7ad6995bad06135
#Test function
from time import ctime
#SQLite interfacing
import sqlite3
from flask import g
<<<<<<< HEAD
=======
#for attachment
from lxml import etree
>>>>>>> 2e6ff0a43b69e6b4f84032b7c7ad6995bad06135

app = Flask(__name__)
enterprise = Enterprise(app)

<<<<<<< HEAD
##################
#DATABASE 
##################

DATABASE = "/home/luca/test.db"
	
	
=======
STRING = enterprise._sp.String
ATTACHMENT = enterprise._sb.Attachment
BOOL = enterprise._sp.Boolean
##################
#DATABASE 
#funzioni di gestione del database, copiate pari pari dalla documentazione
##################
DATABASE = "./test.db"	
>>>>>>> 2e6ff0a43b69e6b4f84032b7c7ad6995bad06135
def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()
<<<<<<< HEAD
		
=======
				
>>>>>>> 2e6ff0a43b69e6b4f84032b7c7ad6995bad06135
def query_db(query, args=(), one=False):
	with app.app_context():
		cur = get_db().execute(query, args)
		rv = cur.fetchall()
		cur.close()
<<<<<<< HEAD
		return (rv[0] if rv else None) if one else rv
=======
		#l'if e levabile e serve per ritornare un solo risultato
		return (rv[0] if rv else None) if one else rv

>>>>>>> 2e6ff0a43b69e6b4f84032b7c7ad6995bad06135
#flask-enterprise forse passa anche gli oggetti ma usiamo le strighe :v
def queryToString(query_result):
	with app.app_context():
		string = ""
		for element in query_result:
			for i in element:
				string += i + " "
			string += "\n"
		return string
<<<<<<< HEAD
		
##################
#WEBSERVICE
##################
class DemoService(enterprise.SOAPService):
	@enterprise.soap(_returns=enterprise._sp.String)
	def get_time(self):
		return ctime()

	@enterprise.soap(enterprise._sp.String,_returns=enterprise._sp.String)
	def get_cane(self,stringa):
		return stringa
		
=======
####
def attQuery(query):
	rv = query_db(query)
	a = ATTACHMENT(data = rv)
	parent = etree.Element('parent')
	ATTACHMENT.to_parent_element(a)
	return 1
		
##################
#WEBSERVICE
#la classe che rappresenta il webservice, ogni metodo ha il decoratore con tipi
#di parametri e return
##################

class DemoService(enterprise.SOAPService):
>>>>>>> 2e6ff0a43b69e6b4f84032b7c7ad6995bad06135
	@enterprise.soap(enterprise._sp.String, _returns=enterprise._sp.String)
	def sendQuery(self, query):
		rv = query_db(query)
		return queryToString(rv)
		
<<<<<<< HEAD
#############
#WEBSITE
=======
	@enterprise.soap(STRING,_returns = BOOL )
	def attcQuery(self,query):
		return attQuery(query)

#############
#WEBSITE
#qui ci sono le app di flask, ho fatto delle provette poi bisognera fare un frontend carino
>>>>>>> 2e6ff0a43b69e6b4f84032b7c7ad6995bad06135
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

<<<<<<< HEAD

@app.route('/cane')
def cane():
	return 'canedio'

if __name__ == '__main__':
	app.debug = True
	app.run()  
=======
@app.route('/attc')
def attc():
	if attQuery("select * from catalogo"):
		element = parent[0]
		print(etree.tostring(element))
		print(ATTACHMENT.from_xml(element).data)
	else:
		print(error)	

if __name__ == '__main__':
	#debug andra tolto
	app.debug = True
	#il tutto viene avviato qui: http://localhost:porta/
	app.run(port = 5000)
>>>>>>> 2e6ff0a43b69e6b4f84032b7c7ad6995bad06135
