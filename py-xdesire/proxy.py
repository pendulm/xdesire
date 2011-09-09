import BaseHTTPServer
import mimetypes
import urllib
import re
import sys

PORT = 8080

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

class ProxyHandle(BaseHTTPServer.BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        try:
            request_page = urllib.urlopen(self.path)
            main_path = re.split('#|\?', self.path, 1)[0]
            mimetype = mimetypes.guess_type(main_path)[0]

            if not mimetype:
                mimetype = 'text/html'

            page_content = request_page.read()
            self.send_response(200)
            self.send_header("Content-type", mimetype)
            self.send_header("Content-Length", len(page_content))
            self.end_headers()
            self.wfile.write(page_content)
        except IOError:
            self.send_error(500)



print "Server start at localhost:%s." % PORT
run(handler_class=ProxyHandle)
