var _url = require('url');
var _http = require('http');
var PORT = 8080;
console.log("server run on port: " + PORT);

_http.createServer(function (request, response) {
  var queryUrl = _url.parse(request.url);
  var options = {
    host: request.headers.host,
    port: parseInt(queryUrl.port) || 80,
    path: request.url
  };
  var getPage = _http.get(options, function(res) {
    console.log(res.statusCode + ' - ' + request.url);
  });

  getPage.on('error', function(e) {
    console.log("Got error: " + e.message);
  });
  
  getPage.on('response', function(clientRes) {
    var ifFirst = true;
    clientRes.on('data', function(chunk) {
      if(ifFirst) {
        response.writeHead(clientRes.statusCode, clientRes.headers);
        ifFirst = false;
      }
      response.write(chunk);
    });

    clientRes.on('end', function() {
      response.end();
    });
  });

}).listen(PORT);
