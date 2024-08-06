from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from urllib.parse import parse_qs
import json
from sheets_handler import add_subscriber, get_subscribers

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/subscribers':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            subscribers = get_subscribers()
            html = "<html><body><h1>Subscribers</h1><ul>"
            for sub in subscribers:
                html += f"<li>{sub['name']} - {sub['email']}</li>"
            html += "</ul></body></html>"
            self.wfile.write(html.encode())
            return
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = parse_qs(post_data)

        name = data.get('name', [''])[0]
        email = data.get('email', [''])[0]

        add_subscriber(name, email)

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
