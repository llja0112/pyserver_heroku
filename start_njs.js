var njs_client = require('./njs_client.js');

njs_client.start_clientjs();
console.log("start");
njs_client.to_bot("send text", function(response){
	console.log("cb from server success", response);

});
