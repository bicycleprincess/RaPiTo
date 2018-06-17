import socket, time, json
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


if __name__ == '__main__':
    server = udpHandler()
    server.handler()

    try:
    	raw_input("UDP server is ready. Hit Enter to stop\n")
    	server.close()
    except SyntaxError:
    	pass
