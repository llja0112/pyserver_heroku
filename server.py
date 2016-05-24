from __future__ import print_function
import os
import logging
import sys
import eliza
from flask import Flask, request, jsonify

app = Flask(__name__)
app.debug = 'DEBUG' in os.environ

@app.route('/')
def index():
    return 'pyserver is running'

@app.route('/process', methods=['GET','POST'])
def process():
    if request.json:
        message = request.json['message']

        # Analyze message here!
        # Eliza analyzer here for example.
        if message == 'hello':
            reply = 'HELLO'
        else:
            reply = 'What did you say?'

        reply = eliza.analyse(message)
        # Example of console printing when debugging
        print(reply, file=sys.stderr)
        # -- End of Eliza analyzer -- #

        return jsonify(reply=reply)
    else:
        return jsonify(status='error')

if __name__ == '__main__':
    # Uncomment next line during development
    app.debug = True
    app.run()
