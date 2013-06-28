from subprocess import check_output
import pickle
import socket

reg_data = {}
reg_data["tty"] = check_output(["tty"]).strip()
reg_data["name"] = "matt"


s = socket.socket()
host = socket.gethostname()
port = 10000

s.connect((host, port))
s.send(pickle.dumps(reg_data))
s.close
