// Hello World Client
// Connects REQ socket to tcp://localhost:5555



// substitue with input from Twitter
var zmq = require('zmq');
//var WebSocket  = require('ws');
//var http = require('http');
//var express = require('express');
//var app = express()
//var port = process.env.PORT||5555

//var exampleSocket = new WebSocket("ws://https://guarded-spire-37973.herokuapp.com:80/data/websocket");
//var exampleSocket = new WebSocket("ws://localhost:5555", "echo-protocol");
//exampleSocket.onopen = function(){
//	console.log("Connection open");
//}

//exampleSocket.onclose=function(){
//	console.log("Connection closed");
//}


//var socket = new WebSocket(this.getUrl());

module.exports = {

	start_clientjs:function(){
		console.log("\n")
		console.log("Connecting to Hello world server");
		global.requester = zmq.socket('req');

		requester.connect("tcp://0.0.0.0:5555");

		process.on('SIGINT', function(){
			requester.close();
		});

	},

	to_bot:function(text, callBack){

		requester.send(text);
		console.log("sent to server:", text);

		requester.on("message", function(reply){
			console.log("Received reply: [", reply.toString(), ']');
			return callBack(reply.toString());
			console.log("Return callback1");
			requester.close();
			process.exit(0);

		});
	}
};


