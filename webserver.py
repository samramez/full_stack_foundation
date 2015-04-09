__author__ = 'samramez'

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

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
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output

                # Finish if Statement
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

            # Checking if the data we're receiving is HTML FORM type
            if ctype == 'multipart/form-data':

                # Collect all of the fields in the form
                fields = cgi.parse_multipart(self.rfile, pdict)

                # Get value from the specific field ('message') from the FORM
                messagecontent = fields.get('message')

            output = ""
            output +=  "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass


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