# #!/usr/bin/env python3
# """Simple HTTP server serving a reveal.js presentation."""
#
# from http.server import HTTPServer, SimpleHTTPRequestHandler
#
#
# class PresentationHandler(SimpleHTTPRequestHandler):
#     def do_POST(self):
#         pass
#
# def run() -> None:
#     # import os; _old = os.getcwd()
#     # os.chdir(os.path.dirname(__file__) or ".")
#     server = HTTPServer(("0.0.0.0", 8000), PresentationHandler)
#     print(f"\nOpen http://localhost:8000\n(Ctrl+C to stop)\n")
#     server.serve_forever()
#
#
# if __name__ == "__main__":
#     run()

import os
import http.server
import socketserver

PORT = 11345

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])

        post_data = self.rfile.read(content_length)

        # print(f"Received POST data: {post_data.decode('utf-8')} Content length: {content_length}")
        prompt = post_data.decode('utf-8')
        res = client.generate(model=MODEL, prompt=prompt, system=data)
        # print(f"\n--- Result ---\n{res["response"]}")


        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # response_message = b"POST request received successfully!"
        response_message = str.encode(res["response"])
        self.wfile.write(response_message)


with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    # Start the server and keep it running until you stop the script
    httpd.serve_forever()