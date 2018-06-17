import pika
import logging, os

# import the real function you want
from threading import Thread

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.httpserver

try:
	import json
except ImportError:
	pass
else:
	import simplejson as json

logging.basicConfig(level=logging.INFO)

clients = []
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
logging.info('connection: localhost')
channel = connection.channel()

def threaded_rmq():
	channel.queue_declare(queue="array")
	logging.info('consumer ready, get the array')
	channel.basic_consume(consumer_callback, queue="array", no_ack=True) 
	channel.start_consuming()

def disconnect_to_rabbitmq():
	channel.stop_consuming()
	connection.close()
	logging.info('Disconnected from Rabbitmq')

def consumer_callback(ch, method, properties, body):
	# your main funcion goes here
	pass

class SocketHandler(tornado.websocket.WebSocketHandler):

	def open(self):
		logging.info('WebSocket opened')
		clients.append(self)

	def on_message(self):
		pass

	def on_close(self):
		logging.info('WebSocket closed')
		clients.remove(self)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")


application = tornado.web.Application([
    (r'/ws', SocketHandler),
    (r"/", MainHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': '/Users/yangwil/ENV/Testbed/Playground/img'}),
  ])

def startTornado():
	application.listen(8080)
	tornado.ioloop.IOLoop.instance().start()

def stopTornado():
	tornado.ioloop.IOLoop.instance().stop()

if __name__ == "__main__":
	logging.info("RabbitMQ starting")
	threadRMQ = Thread(target=threaded_rmq)
	threadRMQ.start()

	logging.info("Server starting")
	threadTornado = Thread(target=startTornado)
	threadTornado.start()

	try:
		raw_input("Server ready. Press enter to stop\n")
	except SyntaxError:
		pass
	try:
		logging.info('Disconnecting')
		disconnect_to_rabbitmq.close()
	except Exception, e:
		pass

	stopTornado()
	logging.info("Bye Bye")
