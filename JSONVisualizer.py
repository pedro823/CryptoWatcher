import http.server

def create_server(server_address = '',
                  server_type = http.server.HTTPServer,
                  handler_type = http.server.SimpleHTTPRequestHandler):
    port_and_adress = (server_address, 8000)
    httpd = server_type(port_and_adress, handler_type)
    httpd.serve_forever()

if __name__ == "__main__":
    create_server()
