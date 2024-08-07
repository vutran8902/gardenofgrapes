from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs
from sheets_handler import add_subscriber

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/thank_you.html':
            self.path = '/thank_you.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = parse_qs(post_data)

        name = data.get('name', [''])[0]
        email = data.get('email', [''])[0]

        # Save user input to secure data center
        add_subscriber(name, email)

        # Redirect to thank you page
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
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs
from sheets_handler import add_subscriber, get_subscribers

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/thank_you.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('thank_you.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/view_subscribers':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            subscribers = get_subscribers()
            self.wfile.write(subscribers.encode())
        else:
            return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = parse_qs(post_data)

        name = data.get('name', [''])[0]
        email = data.get('email', [''])[0]

        # Save user input to secure data center
        add_subscriber(name, email)

        # Send a success response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Subscription successful")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
