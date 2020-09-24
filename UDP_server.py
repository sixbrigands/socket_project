import socket
import sys

host = sys.argv[1]  #server port and address      
port = int(sys.argv[2])  

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind((host, port))

while True:    
    data, addr = s.recvfrom(4096) # buffer size is 4096 bytes
    if not data:
        break
    message = data.decode('utf-8')
    print(message)

    response = s.sendto(data, (addr))