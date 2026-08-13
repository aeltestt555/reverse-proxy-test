import os
from http.server import HTTPServer, BaseHTTPRequestHandler

APP_NAME = os.getenv("APP_NAME", "Unknown")
APP_MESSAGE = os.getenv("APP_MESSAGE", "No message")

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        response = f"""
        <h1>{APP_NAME}</h1>
        <p>{APP_MESSAGE} version  2 deploi </p>
        """

        self.wfile.write(response.encode())
this is broken
HTTPServer(("127.0.0.1", 8000), App).serve_forever()
