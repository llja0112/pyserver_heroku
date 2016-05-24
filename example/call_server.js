/*
  Example code to send post request to python server.
*/
var request = require('request');

// Alternate between localhost and remote address
var serverURL = 'http://localhost:5000';
var serverURL = 'http://localhost:5000';

sendMessage('hello');
sendMessage('How are you?');
sendMessage('I am Anthony.');

function sendMessage(message){
  request.post(
    {
      url: serverURL + '/process',
      json: { message: message }
    },
    function (error, response, body) {
      if (!error && response.statusCode == 200) {
        console.log(body.reply);
      } else {
        console.log(response);
      }
    }
  );
}
