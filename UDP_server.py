import socket
import sys

host = sys.argv[1]  #server port and address      
port = int(sys.argv[2])
ID_arr = []  

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind((host, port))

while True:    
    data, addr = s.recvfrom(4096) # buffer size is 4096 bytes
    if not data:
        break
    message = data.decode('utf-8')
    print(message)
    mess_arr = message.split() #convert to list with [header, connect_ID, host, port]
    connect_ID = int(mess_arr[1])
    #if the connection ID is not in the ID_arr, then return an OK message
    if connect_ID not in ID_arr: 
        ID_arr.append(connect_ID)
        response = "OK " + mess_arr[1] + " " + mess_arr[2] + " " + mess_arr[3]
        s.sendto(bytes(response, 'utf-8'), (addr))

    #else tell the client to reset the connection ID
    else:
        response = "RESET " + mess_arr[1]
        s.sendto(bytes(response, 'utf-8'), (addr))