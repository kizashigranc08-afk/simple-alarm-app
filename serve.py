import os
import http.server
import socketserver

os.chdir("/Users/s.k/Desktop/cloudecodeテスト用")
PORT = 3456
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
