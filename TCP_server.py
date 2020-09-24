#Based on code in this guide: https://docs.python.org/3/library/socket.html

import socket
import sys

host       = sys.arg[2]        #hostname
port       = sys.arg[3]        # Use non-privileged ports > 1023


#AF_INET = IPv4 rather than AF_INET which would be IPv6
#SOCK_STREAM is for a TCP connection, socket.SOCK_DGRAM is for UDP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # a with statement automatically closes the socket when done
    s.bind((host, port)) #associate listening socket s with 'host' IP address at port 'port' 
    s.listen()
    conn, addr = s.accept() #conn is a new socket different to s. s was the listening socket, conn is the connected one
    with conn:
        print('Connected by', addr)
        while True: #infite while loop to endlessly return what client sends
            data = conn.recv(1024) #recieve data in buffer size 1024(max data that can be recieved at once). buffer size should be a smaller power of 2.
            if not data: #not returns true of data = 0, true otherwise
                break    #break from loop when data stops (end of message)
            conn.sendall(data) #send what is recieved back to client