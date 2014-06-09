from flask import Flask
from flask import Flask
from flaskext.enterprise import Enterprise
<<<<<<< HEAD
from suds.client import Client
=======
#credo che questo sia un import superfluo pero boh
from suds.client import Client
from lxml import etree
>>>>>>> 2e6ff0a43b69e6b4f84032b7c7ad6995bad06135

app = Flask(__name__)
enterprise = Enterprise(app)
soap_url = 'http://localhost:5000/_enterprise/soap'
wsdl_url = 'http://localhost:5000/_enterprise/soap?wsdl'
<<<<<<< HEAD

print "---BVR SOAP CLIENT---\n"
print "connecting...",

client = Client(url = wsdl_url, location = soap_url)
#client.options.cache.clear()
print "connected!\n"
while(1):
	query = raw_input("write your query: ")
	if query == "quit": break;
	print "\n" + client.service.sendQuery(query) + "\n"
	
=======
ATT = enterprise._sb.Attachment
print("---BVR SOAP CLIENT---\n")
print("connecting...")

client = Client(url = wsdl_url, location = soap_url)
#suds fa il caching del wsdl, se cambi qualcosa e bene riscaricarlo, quindi va fatto un clear
client.options.cache.clear()
#interfaccina totalmente inutile :v
print("connected!\n")
while(1):
	query = raw_input("write your query: ")
	if query == "quit": break;
	print("\n" + client.service.sendQuery(query) + "\n")
	# if client.service.attQuery(query):
	# 	string = ""
	# 	element = parent[0]
	# 	a = ATT.from_xml(element).data
	# 	for i in a:
	# 		for j in i:
	# 			string += i + " "
	# 		string += "\n"
	# 	print string
	# else:
	# 	print "error"	
>>>>>>> 2e6ff0a43b69e6b4f84032b7c7ad6995bad06135
