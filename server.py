from http.server import HTTPServer, SimpleHTTPRequestHandler

handler = SimpleHTTPRequestHandler
server = HTTPServer(('localhost', 8000), handler)
print("\nPresentation running at: http://localhost:8000")
print("Press Ctrl+C to stop\n")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
