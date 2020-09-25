#Based on code in this guide: https://docs.python.org/3/library/socket.html

import socket
import sys

header     = sys.argv[1]        #lead string such as 'hello'
host       = sys.argv[2]        #hostname
port       = int(sys.argv[3])        # Use non-privileged ports > 1023
connect_ID = sys.argv[4]        #a connection id 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data)) #repr returns a printabled verson of the byte object data