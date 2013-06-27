# The Aim

This one is a bit harder - the challenge is to connect to a server running on the pi at port 12345. We have to send the server the right password to unlock the next step.

The password is the integer number of seconds since midnight, 1st January, 1970. In Linux, this is known as the 'number of seconds since the epoch'

# What you'll need to know...

## How to get the number of seconds since the epoch

the python document on time is here http://docs.python.org/2/library/time.html

## Converting to and from strings, ints and floats

read the entries for float(), int() and str() on the built-in functions page: http://docs.python.org/2/library/functions.html

## Connecting to a TCP server

The more complicated part is connecting to the server. The further reading section below has all the details, but the bare minimum is:

    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 12345                # The port
    s.connect((host, port))     # Connect
    s.send(some_thing)          # Send something
    s.close                     # Close the socket

# Further reading

http://docs.python.org/2/howto/sockets.html
