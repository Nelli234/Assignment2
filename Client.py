# runs on Pi

import socket
from time import sleep as sl
s = socket.socket()
host = '10.102.13.79'# ip of rapberry pi, running the server
port = 5000
s.connect((host, port))


print(s.recv(1024).decode('utf-8'))
s.close()


print("All done")