#based on code from: https://wiki.python.org/moin/UdpCommunication

import socket
import sys

header     = sys.argv[1]        #lead string such as 'hello'
host       = sys.argv[2]        #hostname
port       = int(sys.argv[3])
connect_ID = sys.argv[4]        #a connection id 
message    = header + " " + connect_ID

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.sendto(bytes(message, 'utf-8'), (host, port))