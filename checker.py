#!/usr/bin/python
"""
checks that the stages have been completed, and creates the new clues
"""

import pickle
import socket
import time
from PIL import Image, ImageDraw
import BaseHTTPServer
import urlparse

state_file = '/tmp/.adventure_state'

root_dir = '/tmp/adventure/'

#stage 1 - check for 100 files
def check_stage_1():
    try:
        for file_num in range(1,100):
            file_name = root_dir + 'stage1/' + str(file_num)
            file_handle = open(file_name)
            lines = len(file_handle.readlines())
            if lines != file_num:
                raise Exception("wrong number of lines")
        print "passed"
        return True
    except Exception, e:
        print "failed", e 
    return False

def check_stage_2():
    try:
        file_name = root_dir + 'stage2/image.png'
        img = Image.open(file_name)
        colors = img.getcolors(10)
        count = 0
        for color in colors:
            if color[1] == (255,0,0):
                count +=1
            if color[1] == (0,255,0):
                count +=1
            if color[1] == (0,0,255):
                count +=1
        if count == 3:
            print "passed"
            return True
    except Exception, e:
        print "failed", e
    return False

def check_stage_3():
    try:
        s = socket.socket()         # Create a socket object
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = socket.gethostname() # Get local machine name
        port = 12345                # Reserve a port for your service.
        s.bind((host, port))        # Bind to the port

        s.listen(5)                 # Now wait for client connection.
        while True:
            c, addr = s.accept()     # Establish connection with client.
            print 'Got connection from', addr
            data = c.recv(1024)
            if data:
                print "got", data
                try:
                    sent_time = float(data)
                    if int(sent_time) == int(time.time()):
                        print "passed"
                        c.close()
                        return True
                except ValueError:
                    pass
    except Exception, e:
        print "failed", e
        c.close()
    return False

def check_stage_4():
    try:
        file_name = root_dir + 'stage4/file.txt'
        fd = open(file_name)
        lines = fd.readlines()
        if len(lines) != 100:
            print "wrong number of lines"
            return False
        expecting = 'raspberry'
        for line in lines:
            line = line.strip()
            if line != expecting:
                print "line wasn't correct"
                print line
                return False
            if expecting == 'raspberry':
                expecting = 'pi'
            else:
                expecting = 'raspberry'
        print "passed"
        return True
    except IOError:
        print "no file"
        return False
    return False




class MyHTTPServer(BaseHTTPServer.HTTPServer):
    def __init__(self,server_address, RequestHandlerClass,code):
        BaseHTTPServer.HTTPServer.__init__(self, server_address, RequestHandlerClass)
        self.code = code
        print "code:", code

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Password Page</title></head>")
        s.wfile.write("<body><p>challenge=" + str(s.server.code) + "</p>")
        s.wfile.write("</body></html>")

    def do_POST(s):
        length = int(s.headers['Content-Length'])
        post_data = urlparse.parse_qs(s.rfile.read(length).decode('utf-8'))
        if post_data.has_key('response'):
            try:
                response = int(post_data['response'][0])
                if response == s.server.code * 2:
                    print "pass"
                    s.send_response(200)
                    s.send_header("Content-type", "text/html")
                    s.end_headers()
                    #kill the server
                    s.server.socket.close()
                else:
                    print "wrong code:", response
                    s.send_response(500)
            except ValueError:
                print "couldn't parse response"
                s.send_response(500)
        else:
            print "no response arg"
            s.send_response(500)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def server_bind(self):
        MyHTTPServer.server_bind(self)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

def check_stage_5():
    host = socket.gethostname()
    port = 8080
    httpd = MyHTTPServer((host,port),MyHandler,1010011)
    try:
        httpd.serve_forever()
    except socket.error:
        httpd.server_close()
        print "passed"
        return True

##################
try:
    stage = pickle.load(open(state_file))
except IOError:
    stage = 1


print "stage:", stage
if stage == 1:
    if check_stage_1():
        stage +=1
elif stage == 2:
    if check_stage_2():
        stage +=1
elif stage == 3:
    if check_stage_3():
        stage +=1
elif stage == 4:
    if check_stage_4():
        stage +=1
elif stage == 5:
    if check_stage_5():
        stage +=1


state_file = open(state_file,'w')
pickle.dump(stage,state_file)
