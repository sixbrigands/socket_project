#Based on code in this guide: https://docs.python.org/3/library/socket.html

import socket
import sys
import threading
import os

header     = sys.argv[1]        #lead string such as 'hello'
host       = sys.argv[2]        #hostname
port       = int(sys.argv[3])
connect_ID = sys.argv[4]        #a connection id 
attempt    = 3

#A function to handle connection errors.
def connection_error():
    global attempt
    global connect_ID
    #when 3 attempts runs out, print failure and exit
    attempt -= 1
    if (attempt <= 0):
        print("Connection Failure") 
        os._exit(0)
    print('Connection Error ' + connect_ID)
    connect_ID = input("Enter a new connection ID: ")
    client()

def client():
    global attempt
    global connect_ID

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        message = header + " " + connect_ID + " " + host + " " + str(port) #build message
        try:
            s.connect((host, port))
            s.sendall(bytes(message, 'utf-8'))
        except:
            connection_error()

        #start timer
        timeout = threading.Timer(60, connection_error)
        timeout.start()
        data = s.recv(1024) #take in response from server
        if data:
            timeout.cancel()
            message = data.decode('utf-8')
            mess_arr = message.split() #convert to list with [header, connect_ID, host, port] (no host, port if header = RESET)
            status = mess_arr[0]

            connect_ID = mess_arr[1]
            
            #print this if successfully connected to server
            if (status == 'OK'):
                print('Connection established ' + connect_ID + " " + mess_arr[2] + " " + mess_arr[3])
            else:
                connection_error()


if __name__ == "__main__": 
    client()