from http.server import HTTPServer, BaseHTTPRequestHandler

url_dict = {"google": "https://www.google.com"}


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/test.html'
        try:
            print(self.path[1:])
            if self.path[1:] in url_dict.keys():
                self.send_response(301)
                self.send_header('Location', url_dict[self.path[1:]])
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


if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8080), Serv)
    httpd.serve_forever()
