#based on code from: https://wiki.python.org/moin/UdpCommunication

import socket
import sys

header     = sys.argv[1]        #lead string such as 'hello'
host       = sys.argv[2]        #hostname
port       = int(sys.argv[3])
connect_ID = sys.argv[4]        #a connection id 
message    = header + " " + connect_ID + " " + host + " " + str(port)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
    s.sendto(bytes(message, 'utf-8'), (host, port))
    data, server = s.recvfrom(4096)
    print(data.decode("utf-8"))