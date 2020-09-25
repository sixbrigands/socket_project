#based on code from https://wiki.python.org/moin/UdpCommunication

import socket
import sys
import threading
import os

def closeConnection():
    print("Connection Timeout")
    s.close()
    os._exit(0)

host = sys.argv[1]  #server port and address      
port = int(sys.argv[2])
ID_arr = []
timeout_length = 300.0  

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind((host, port))
timeout = threading.Timer(timeout_length, closeConnection)
timeout.start()
print("no data yet, timer started")
while True:    
    data, addr = s.recvfrom(4096) # buffer size is 4096 bytes 
    if data:
        print('timer cancelled')
        timeout.cancel()
        message = data.decode('utf-8')
        print(message)
        mess_arr = message.split() #convert to list with [header, connect_ID, host, port]
        connect_ID = int(mess_arr[1])

        #if the connection ID is not in the ID_arr, add it to the array for 1 minute and then return an OK message
        if connect_ID not in ID_arr: 
            ID_arr.append(connect_ID)
            t = threading.Timer(60.0, ID_arr.pop, [0]) #after a minute, remove the first element in the array
            t.start()
            response = "OK " + mess_arr[1] + " " + host + " " + str(port)
            s.sendto(bytes(response, 'utf-8'), (addr))

        #else tell the client to reset the connection ID
        else:
            response = "RESET " + mess_arr[1]
            s.sendto(bytes(response, 'utf-8'), (addr))

        timeout = threading.Timer(timeout_length, closeConnection)
        timeout.start()
        print("timout restarted!")

