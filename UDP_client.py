import socket
import sys

header     = sys.argv[1]        #lead string such as 'hello'
host       = sys.argv[2]        #hostname
port       = int(sys.argv[3])        # Use non-privileged ports > 1023
connect_ID = int(sys.argv[4])        #a connection id 
message    = [header, connect_ID]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.sendto(message, (host, port))