from http.server import BaseHTTPRequestHandler, HTTPServer

from datetime import datetime

import logging
import requests
import socket
import ssl
import time

class Server(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        min = datetime.now().strftime('%M')
        resp = requests.get("http://google.com")
        array = ["something"]
        self._set_response()
        self.wfile.write(f"GET request for\npath: {self.path}\nheaders: {array}\nfrom {socket.gethostname()}\ngoogle.com resp:\n{resp.content}".encode('utf-8'))

    def do_POST(self):
        if self.path != '/some/path':
            self.send_response(404)
            return
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {} from {}".format(self.path, socket.gethostname()).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=Server):
    """Entrypoint for python server"""
    server_address = ("0.0.0.0", 80)
    httpd = server_class(server_address, handler_class)

    # to generate private key:
    #    $ openssl genrsa -out "rsa_2048_priv.pem" 2048
    # to generate public key
    #    $ openssl rsa -in "rsa_2048_priv.pem" -pubout -out "rsa_2048_pub.pem"
    #httpd.socket = ssl.wrap_socket (httpd.socket,
    #    keyfile="/Users/sfeldstein/workspace/py-simple-server/rsa_2048_priv.pem",
    #    certfile='/Users/sfeldstein/workspace/py-simple-server/rsa_2048_pub.pem', server_side=True)

    print("launching server...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
