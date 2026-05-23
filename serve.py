import os
import http.server
import socketserver

os.chdir("/Users/s.k/Desktop/cloudecodeテスト用")
PORT = int(os.environ.get("PORT", 3456))
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
