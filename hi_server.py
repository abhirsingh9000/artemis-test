from http.server import BaseHTTPRequestHandler, HTTPServer

class HiServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hi!')

def run_server():
    server_address = ('', 80)  # Listen on port 80
    httpd = HTTPServer(server_address, HiServer)
    print('Starting server on port 80...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
