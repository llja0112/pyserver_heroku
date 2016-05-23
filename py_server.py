#
# Binds REP socket to tcp://*:5555
# Expects b"Hello" from client. Replies with b"World"
import time
import zmq
import eliza
#import botOrNot
import nltk
import sys
import socket as SOCKET

def init():

	print("start pyserver")
	sys.stdout.flush()
	context = zmq.Context()
	socket = context.socket(zmq.REP)
#	socket.bind("ws://http://guarded-spire-37973.herokuapp.com:80/data/webserver")
#	hostname = "localhost"
#	hostname="http://guarded-spire-37973.herokuapp.com"
#	ip_address = SOCKET.gethostbyname(hostname)
#	print ip_address
#	socket.bind("tcp://guarded-spire-37973.herokuapp.com/5555/webserver")

#	socket.bind("tcp://*:5555/chat")
	socket.bind("tcp://0.0.0.0:5555")

#	x = zmq.socket(socket)
#	print x
#	socket.bind("tcp://0.0.0.0:5555")
#	This has to change later at some point

	while True:
		message = socket.recv()
		print("Received request 1")

	# if deregotary term, send that's not very nice.
	# are you a bot questions?
		print(message)
		message = message.split()
		#ANALYSE MESSAGE

#		if "yes" in message:
#			print("yes response")
#		if "no" in message:
#			print("no response")

#		for word in message:
#			if word in emotions_list:
#				print("emotion detected:", word)
#
#			if word in w5h1:
#				print("w5h1 detected:", word)

				#find_response_from_dict
				#response_dict[theme][question]
				#read response_dict from excel sheet


	# if unsure, send eliza response
#		eliza_response = eliza.analyse(message)
	#STrip the @ sign.
		print("Received request: %s" % message)

		time.sleep(0)
#		socket.send(b":"+eliza_response)
		socket.send(b":"+"-".join(message))

init()

class Conversation(object):
#check theme
#check convesation style/nature
#check if talking to friend or colleague
	def __init__(self, theme):
		self.theme = theme


	def setQuestion(ques):
		self.ques = ques

	def setTheme(theme):
		self.theme = theme

	def getTheme():
		return self.theme



