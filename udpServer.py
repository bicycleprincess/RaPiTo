import socket, time, json
#import dpkt
#import numpy as numpy
import logging

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_IP = '127.0.0.1'
UDP_PORT = 31588 	# port conflict
BUFFER_SIZE = 2048

class udpHandler(object):
	
	def __init__(self):
		pass

	def handler(self):
		s.bind((UDP_IP, UDP_PORT))	
		print "******* UDP server started *******"

	#def close(self):
	#	s.close()
'''
	#gw1 = {'MAC':'c4:2c:03:30:a5:fe', 'latitude':52.49782, 'lontitude':13.3051813, 'hight': 5}
	#gw2 = {'MAC':'d8:a2:5e:96:57:7a', 'latitude':52.5414599, 'lontitude':13.3502726, 'hight': 8}
	#gw3 = {'MAC':'0a:a2:5e:96:57:7a', 'latitude':52.5016021, 'lontitude':13.3388043, 'hight': 20}
	#gw4 = {'MAC':'60:33:4b:ff:fe:8a:71:e2', 'latitude':52.5209312, 'lontitude':13.2781041, 'hight': 14}
	#gw5 = {'MAC':'fe80::daa2:5eff:fe96:577a', 'latitude':52.5125322, 'lontitude':13.3247559, 'hight': 7}
'''

#if __name__ == '__main__':
#	gen = arrayGenerator()
#	gen.getGWInfo()


'''
if __name__ == '__main__':
    server = udpHandler()
    server.handler()
    #logging.info("Server started")
    #print "Server started"

    try:
    	raw_input("UDP server is ready. Hit Enter to stop\n")
    	server.close()
    except SyntaxError:
    	pass
'''
    #gw = arrayGenerator()
