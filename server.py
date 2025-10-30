import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "images"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Access images at http://localhost:{PORT}/<nom_de_votre_image>.png")
    httpd.serve_forever()
