from pymongo import MongoClient

client = MongoClient()

db = client.test

gateways = db.gateways

#for gw in gateways.find():
#	print gw

#print gateways.find_one({"borough" : "Charottenburg"})
#print gateways.find_one({"address.MAC": "fe80::daa2:5eff:fe96:577a"})
gw = gateways.find_one({"address.MAC": "fe80::daa2:5eff:fe96:577a"})
#print gw['address']['latlon']
latlon = gw['address']['latlon']
print type(latlon) 	#list