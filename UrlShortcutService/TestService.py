#!/usr/bin/env python3.9

from http.server import HTTPServer, BaseHTTPRequestHandler
import configparser
import logging


class Serv(BaseHTTPRequestHandler):

    url_dict = {}

    def load_config(self):
        config = configparser.RawConfigParser()
        config.read('config.properties')
        self.url_dict = config['UrlDictionary']

    def do_GET(self):
        # Load urls only once
        if self.url_dict.__len__() == 0:
            self.load_config()

        if self.path == '/':
            self.path = '/test.html'
        try:
            # If shortcut is available in url dictionary then Redirect to it's URL
            if self.path[1:] in self.url_dict.keys():
                self.send_response(301)
                self.send_header('Location', self.url_dict[self.path[1:]])
                self.end_headers()
            else:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))

        except:
            file_to_open = "URL Shortcut not found"
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        # Prepare & send response message
        self.path = '/test.html'
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("POST request for {}".format(self.path), 'utf-8'))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    httpd = HTTPServer(('go', 8080), Serv)
    httpd.serve_forever()
