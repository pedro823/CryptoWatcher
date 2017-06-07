#!/usr/bin/env python3
import http.server

def create_server(server_address = '',
                  server_type = http.server.HTTPServer,
                  handler_type = http.server.SimpleHTTPRequestHandler):
    port_and_adress = (server_address, 8000)
    httpd = server_type(port_and_adress, handler_type)
    print("You can now visit the visualizer at http://localhost:8000.")
    httpd.serve_forever()

if __name__ == "__main__":
    create_server()
