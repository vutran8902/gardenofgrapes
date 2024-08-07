from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs
from sheets_handler import add_subscriber
import json
import traceback

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/thank_you.html':
            self.path = '/thank_you.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = parse_qs(post_data)

            name = data.get('name', [''])[0]
            email = data.get('email', [''])[0]

            # Save user input to secure data center
            add_subscriber(name, email)

            # Send a successful response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success'}).encode())
        except Exception as e:
            print(f"Error in do_POST: {str(e)}")
            print(traceback.format_exc())
            self.send_error(500, f"Internal Server Error: {str(e)}")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
