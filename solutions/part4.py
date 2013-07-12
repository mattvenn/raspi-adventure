import socket               # Import socket module
import time
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
int_time = str(int(time.time()))
print s.send(int_time)
s.close    
