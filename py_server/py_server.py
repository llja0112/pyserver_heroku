#
# Binds REP socket to tcp://*:5555
# Expects b"Hello" from client. Replies with b"World"
import time
import zmq
import eliza
#import botOrNot
import nltk

def init():
	print("start pyserver")
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind("tcp://127.0.0.1:5555")

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
#		socket.send(b":"+"-".join(message))

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



