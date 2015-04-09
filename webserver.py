__author__ = 'samramez'

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class webserverHandler(BaseHTTPRequestHandler):

    # Handles all the GET requests our server receives
    def do_GET(self):
        try:
            # path is variable in BaseHTTPRequestHandler class
            # it holds the client's url in the server
            if self.path.endswith("/hello"):

                # Indicates Successful GET request
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                # What we're sending back to client
                output = ""
                output += "<html><body><h1>Hello!</h1></body></html>"
                self.wfile.write(output)
                print output

                # Finish if Statement
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                message = ""
                message += "<html><body> &#161 Hola ! </body></html>"
                self.wfile.write(message)
                print message
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)


# Instantiate the server
# What ports to listen
def main():
    try:
        port = 8080
        server = HTTPServer(('',port), webserverHandler)
        print "Web server running on port %s" % port

        # Constantly listen until we hit ^+C or exit the application
        server.serve_forever()

    except KeyboardInterrupt:
        # Happens when user hold ^+C on keyboard
        print "^C entered, stopping web server :-P "

        # Shutting down the server
        server.socket.close()

# What code to execute based on type of HTTPServer it has received

if __name__ == '__main__':
    main()