#!/usr/bin/python
"""
checks that the stages have been completed, and creates the new clues

bugs:
if more than 1 person is playing, there is a problem with level3 and sockets being closed.
"""

import pickle
import thread
import socket
import time
import logging
import argparse
from PIL import Image, ImageDraw
import BaseHTTPServer
import urlparse
from subprocess import check_output
import daemon


num_stages = 5

def send_message(reg_data,mesg):
    #TODO change to pi for user
    output=check_output("echo " + mesg + "| write " + reg_data["username"] + " " + reg_data["tty"], shell=True)

def init_next_stage(reg_data):
    
    #increment stage
    reg_data["stage"] += 1
    logger.info("stage now %d for %s" % (reg_data["stage"], reg_data["name"]))

    #create paths and copy files
    path = args.target_dir + reg_data["name"]
    stage_path = "/part" + str(reg_data["stage"])
    reg_data["cwd"] = path + stage_path

    if reg_data["stage"] <= num_stages:
        logger.info( "creating new dir:" + reg_data["cwd"])
        output=check_output(["mkdir","-p",path + stage_path])
        output=check_output(["cp",args.root_dir+stage_path+"/README.md",reg_data["cwd"]])

    #send a message
    if reg_data["stage"] == 1:
        message = "Welcome, " + reg_data["name"] + ". Change to " + reg_data["cwd"] + " and read the README.md to get started"
    elif reg_data["stage"] == 6:
        message = "Well done! You finished the game!"
    else:
        message = "Well done! Now change to %s for the next stage!" % reg_data["cwd"]

    send_message(reg_data,message)
    logger.info("sent message")

    

#a new thread for each adventurer
def start_adventure(reg_data):
    try:
        init_next_stage(reg_data)
        while True:
            logger.info( "checking :"+ str(reg_data))
            if reg_data["stage"] == 1:
                if check_stage_1(reg_data):
                    init_next_stage(reg_data)
            elif reg_data["stage"] == 2:
                if check_stage_2(reg_data):
                    init_next_stage(reg_data)
            elif reg_data["stage"] == 3:
                if check_stage_3(reg_data):
                    init_next_stage(reg_data)
            elif reg_data["stage"] == 4:
                if check_stage_4(reg_data):
                    init_next_stage(reg_data)
            elif reg_data["stage"] == 5:
                if check_stage_5(reg_data):
                    init_next_stage(reg_data)
                    break
            time.sleep(5)
    except Exception, e:
        logger.warn("unhandled exception:" + str(e) )
        exit(1)
        

def check_stage_1(reg_data):
    try:
        file_name = reg_data["cwd"] + '/file.txt'
        fd = open(file_name)
        lines = fd.readlines()
        if len(lines) != 100:
            logger.info("wrong number of lines")
            return False
        expecting = 'raspberry'
        for line in lines:
            line = line.strip()
            if line != expecting:
                logger.info( "line wasn't correct")
                return False
            if expecting == 'raspberry':
                expecting = 'pi'
            else:
                expecting = 'raspberry'
        return True
    except IOError:
        logger.info( "no file")
        return False
    return False

#stage 2 - check for 100 files
def check_stage_2(reg_data):
    try:
        for file_num in range(1,100):
            file_name = reg_data["cwd"] + '/' + str(file_num)
            file_handle = open(file_name)
            lines = len(file_handle.readlines())
            if lines != file_num:
                raise Exception("wrong number of lines on file", file_num)
        return True
    except Exception, e:
        logger.info( "failed:" + str(e) )
    return False

def check_stage_3(reg_data):
    try:
        file_name = reg_data["cwd"] + '/image.png'
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
            return True
    except Exception, e:
        logger.info( "failed:"+ str(e))
    return False

def check_stage_4(reg_data):
    try:
        s = socket.socket()         # Create a socket object
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = socket.gethostname() # Get local machine name
        port = 12345                # Reserve a port for your service.
        s.bind((host, port))        # Bind to the port

        s.listen(5)                 # Now wait for client connection.
        while True:
            c, addr = s.accept()     # Establish connection with client.
            logger.info( 'got connection from'+ str(addr))
            data = c.recv(1024)
            if data:
                logger.info( "got:"+ str(data))
                try:
                    sent_time = float(data)
                    if int(sent_time) == int(time.time()):
                        c.close()
                        return True
                except ValueError:
                    pass
    except Exception, e:
        logger.info( "failed:"+ str(e))
        c.close()
    return False




class MyHTTPServer(BaseHTTPServer.HTTPServer):
    def __init__(self,server_address, RequestHandlerClass,code):
        BaseHTTPServer.HTTPServer.__init__(self, server_address, RequestHandlerClass)
        self.code = code
#        logger.info( "code:"+ code)

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
                    s.send_response(200)
                    s.send_header("Content-type", "text/html")
                    s.end_headers()
                    #kill the server
                    s.server.socket.close()
                else:
                    logger.info( "wrong code:"+ response)
                    s.send_response(500)
            except ValueError:
                logger.info( "couldn't parse response")
                s.send_response(500)
        else:
            logger.info( "no response arg")
            s.send_response(500)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def server_bind(self):
        MyHTTPServer.server_bind(self)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

def check_stage_5(reg_data):
    host = socket.gethostname()
    port = 8080
    httpd = MyHTTPServer((host,port),MyHandler,1010011)
    try:
        httpd.serve_forever()
    except socket.error:
        httpd.server_close()
        return True

##################

def main():
    logger.info("started adventure checker")
    s = socket.socket()         # Create a socket object
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname() # Get local machine name
    port = 10000                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    s.listen(5)                 # Now wait for client connection.
    while True:
        c, addr = s.accept()     # Establish connection with client.
        logger.info( 'got connection from ' + str(addr))
        data = c.recv(1024)
        if data:
            reg_data = pickle.loads(data)
            reg_data["stage"] = 0
            logger.info(reg_data)
            thread.start_new_thread(start_adventure,(reg_data,))

#need to sort this out, at least add some logging!
logger = logging.getLogger("log")
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/tmp/log.file")
logger.addHandler(handler)
handler.setFormatter(formatter)
daemon_context = daemon.DaemonContext(files_preserve=[handler.stream])

#command line args
parser = argparse.ArgumentParser(description='adventure checker')
parser.add_argument('--root-dir', help='where the directory is', default="/home/pi/.raspi-adventure/")
parser.add_argument('--target-dir', help='where the game is played', default="/tmp/adventure/")

args = parser.parse_args()
#with daemon_context:
main()
