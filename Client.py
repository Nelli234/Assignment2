#on PC
#Nelson Hucklebridge
#tprg 2131-01
#2023-11-28
#This program recieves JSON objects from a raspberry pi and prints it on pc
import socket
from time import sleep as sl
s = socket.socket()
host = '10.102.13.79'# ip of rapberry pi, running the server
port = 5000

if __name__ == "__main__":#Main gaurd to exit gracefully 
    try:
        s.connect((host, port))
        print(s.recv(1024).decode('utf-8'))#decodes byte
        s.close()#exits
        print("All done")
    except KeyboardInterrupt:#use CTRL-C
        print("exiting")
    