#based on code from: https://wiki.python.org/moin/UdpCommunication

import socket
import sys
import threading
import os

header     = sys.argv[1]        #lead string such as 'hello'
host       = sys.argv[2]        #hostname
port       = int(sys.argv[3])
connect_ID = sys.argv[4]        #a connection id 
attempt    = 3

def connection_error():
    global attempt
    global connect_ID
    print('Connection Error ' + connect_ID)
    connect_ID = input("Enter a new connection ID: ")
    attempt -= 1
    client()


def client():
    global attempt
    global connect_ID
    if (attempt <= 0):
        print("Connection Failure")
        os._exit(0)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
        message = header + " " + connect_ID + " " + host + " " + str(port) #build message
        s.sendto(bytes(message, 'utf-8'), (host, port))
        timeout = threading.Timer(60, connection_error)
        timeout.start()
        data, server = s.recvfrom(4096)
        if data:
            timeout.cancel()
            message = data.decode('utf-8')
            mess_arr = message.split() #convert to list with [header, connect_ID, host, port] (no host, port if header = RESET)
            status = mess_arr[0]

            connect_ID = mess_arr[1]
            
            if (status == 'OK'):
                print('Connection established ' + connect_ID + " " + mess_arr[2] + " " + mess_arr[3])
            else:
                connection_error()


if __name__ == "__main__": 
    client() 