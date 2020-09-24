#Based on code in this guide: https://docs.python.org/3/library/socket.html

import socket
import sys

header     = sys.arg[1]        #lead string such as 'hello'
host       = sys.arg[2]        #hostname
port       = sys.arg[3]        # Use non-privileged ports > 1023
connect_ID = sys.arg[4]        #a connection id 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data)) #repr returns a printabled verson of the byte object data