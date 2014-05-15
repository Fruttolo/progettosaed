from flask import Flask
from flask import Flask
from flaskext.enterprise import Enterprise
from suds.client import Client

app = Flask(__name__)
enterprise = Enterprise(app)
soap_url = 'http://localhost:5000/_enterprise/soap'
wsdl_url = 'http://localhost:5000/_enterprise/soap?wsdl'

print "---BVR SOAP CLIENT---\n"
print "connecting...",

client = Client(url = wsdl_url, location = soap_url)
#client.options.cache.clear()
print "connected!\n"
while(1):
	query = raw_input("write your query: ")
	if query == "quit": break;
	print "\n" + client.service.sendQuery(query) + "\n"
	
