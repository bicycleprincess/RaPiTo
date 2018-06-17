#from arrayGenerator import *
from udpServer import *

import numpy as np
#import pika, time

try:
	import json
except ImportError:
	pass
else:
	import simplejson as json

filepath = 'gateways.json'

def connecter():

	handler = udpHandler()
	conn = handler.handler()

def arrayGen():

	f = open(filepath, 'r')
	ary = np.ndarray((1,4))
		
	for i in range(5):
		for line in f:
			gw = json.loads(line)
			l = []
			l.append(gw['x'])
			l.append(gw['y'])
			l.append(gw['z'])
			data, addr = s.recvfrom(BUFFER_SIZE)
			ts = time.time()*1e-7
			l.append(ts)
			ary = np.append(ary, l)
	#print type(ary)
	#return ary.reshape(4,6)[:, 1:6]
	res = ary.reshape(6,4)[1:6, :]
	print res
	print ''
	#return res
	print res
	f.close()


if __name__ == '__main__':
	arrayGen()	
"""
def array2json(array):
	'''array format function:

		to json'''
	list = np.chararray.tolist(array)
	return json.dumps(list)

if __name__ == '__main__':
	logging.basicConfig()
	connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))

	while connection.is_open:
	
		print 'Connecting localhost'
		break 
	connecter()

	for i in range(30):
		array = arrayGen()
		jsarray = array2json(array)
	
		synchannel = connection.channel()
		synchannel.queue_declare(queue="array")
		synchannel.basic_publish(exchange='',
    	                  routing_key='array',
    	                  body=jsarray)
		time.sleep(1)

	connection.close()
"""