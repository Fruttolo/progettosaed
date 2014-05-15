from flask import Flask
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

##################
#DATABASE 
##################

DATABASE = "/home/luca/test.db"
	
	
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
		
def query_db(query, args=(), one=False):
	with app.app_context():
		cur = get_db().execute(query, args)
		rv = cur.fetchall()
		cur.close()
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
##################
class DemoService(enterprise.SOAPService):
	@enterprise.soap(_returns=enterprise._sp.String)
	def get_time(self):
		return ctime()

	@enterprise.soap(enterprise._sp.String,_returns=enterprise._sp.String)
	def get_cane(self,stringa):
		return stringa
		
	@enterprise.soap(enterprise._sp.String, _returns=enterprise._sp.String)
	def sendQuery(self, query):
		rv = query_db(query)
		return queryToString(rv)
		
#############
#WEBSITE
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


@app.route('/cane')
def cane():
	return 'canedio'

if __name__ == '__main__':
	app.debug = True
	app.run()  
