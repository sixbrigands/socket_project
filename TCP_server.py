#based on code from https://wiki.python.org/moin/UdpCommunication

import socket
import sys
import threading
import os

host = sys.argv[1]  #server port and address      
port = int(sys.argv[2])
ID_arr = []
timeout_length = 300.0  

def shutdown_gracefully():
    print("Connection Timeout")
    os._exit(0)

def close_connection(conn):
    global ID_arr
    ID_arr.pop(0)
    conn.close()
    main()

def main():
    global ID_arr
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        timeout = threading.Timer(timeout_length, shutdown_gracefully)
        timeout.start()
        s.listen()
        conn, addr = s.accept() #conn is a new socket different to s. s was the listening socket, conn is the connected one
        with conn:    
            data = conn.recv(1024) #recieve data in buffer size 1024
            if data: 
                timeout.cancel()
                message = data.decode('utf-8')
                print(message)
                mess_arr = message.split() #convert to list with [header, connect_ID, host, port]
                connect_ID = int(mess_arr[1])

                #if the connection ID is not in the ID_arr, add it to the array for 1 minute and then return an OK message
                if connect_ID not in ID_arr: 
                    ID_arr.append(connect_ID)
                    t = threading.Timer(60.0, close_connection, [conn]) #after a minute, remove the first element in the array
                    t.start()
                    response = "OK " + mess_arr[1] + " " + host + " " + str(port)
                    conn.sendto(bytes(response, 'utf-8'), (addr))

                #else tell the client to reset the connection ID
                else:
                    response = "RESET " + mess_arr[1]
                    conn.sendto(bytes(response, 'utf-8'), (addr))

                timeout = threading.Timer(timeout_length, shutdown_gracefully)
                timeout.start()
                print("timout restarted!")
                

if __name__ == "__main__":
    main()