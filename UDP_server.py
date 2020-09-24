import socket
import sys

host = sys.argv[1]        
port = int(sys.argv[2])  

s = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((host, port))
    
while True:
    data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)