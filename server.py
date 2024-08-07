from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from urllib.parse import parse_qs
import json
from sheets_handler import add_subscriber, update_subscribers_file

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = parse_qs(post_data)

        name = data.get('name', [''])[0]
        email = data.get('email', [''])[0]

        add_subscriber(name, email)
        update_subscribers_file()

        self.send_response(303)
        self.send_header('Location', '/thank_you.html')
        self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
