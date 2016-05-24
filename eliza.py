import re
import random
import json

def init():
	print "Eliza module activated"

	global reflections
	global psychobabble

	with open('./dict/reflections.json') as fi:
		reflections = json.load(fi)

	with open('./dict/psychobabble.txt', 'r') as fi:
		psychobabble = eval(fi.read())

def analyse(from_human):

	from_human = " ".join(from_human.split()[1:])
	for pattern, responses in psychobabble:
		match = re.match(pattern, from_human.rstrip(".!"))
		if match:
			print "match!"
			response = random.choice(responses)
			return response.format(*[reflect(g) for g in match.groups()])


def reflect(fragment):
	tokens = fragment.lower().split()
	for i, token in enumerate(tokens):
		if token in reflections:
			tokens[i] = reflections[token]

	return " ".join(tokens)



init()
