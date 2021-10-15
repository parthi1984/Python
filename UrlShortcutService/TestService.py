#!/usr/bin/env python3.9

from http.server import HTTPServer, BaseHTTPRequestHandler
import configparser
import urllib.parse
import logging


class Serv(BaseHTTPRequestHandler):

    url_dict = {}
    queryString = {}

    def load_config(self, method='GET'):
        config = configparser.RawConfigParser()
        config.read('config.properties')
        self.url_dict = config['UrlDictionary']

        if method == 'POST':
            if self.queryString['shortKey'][0] in self.url_dict.keys():
                return 'ShortKey already existing!!!'
            else:
                config.set('UrlDictionary', self.queryString['shortKey'][0], self.queryString['longLink'][0])
                with open('config.properties', 'w') as configFile:
                    config.write(configFile)
                return 'ShortKey Added.'
        else:
            return 'Data loaded.'

    def do_GET(self):
        resp = self.load_config()
        logging.info(resp)

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
                file_to_open = file_to_open.replace('{hidden}', '')
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
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
        # logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        #              str(self.path), str(self.headers), post_data.decode('utf-8'))
        self.queryString = urllib.parse.parse_qs(post_data.decode('utf-8'))
        resp = self.load_config(method='POST')
        logging.info(resp)

        # Prepare & send response message
        self.path = '/test.html'
        file_to_open = open(self.path[1:]).read()
        file_to_open = file_to_open.replace('{hidden}', resp)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    httpd = HTTPServer(('go', 8080), Serv)
    httpd.serve_forever()
