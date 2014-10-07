import SimpleHTTPServer
import SocketServer

PORT = 8888


class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()

        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")


def d3server():

    Handler = MyHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    httpd.serve_forever()
