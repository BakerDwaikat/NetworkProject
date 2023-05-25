import time
from socket import * #Import all functions from socket library
serverPort = 8855 #Set the server port to 8855
serverSocket = socket(AF_INET, SOCK_DGRAM) #Create a server socket with address family (here its IPv4) and type of socket (here its UDP socket)
serverName = '192.168.95.159'  #Get the local host name or IP address and store it in variable "serverName"
serverSocket.bind((serverName, serverPort)) #assigns the port number 5566 to the server’s socket
print ('The server is ready to receive')
clients = set()
while True: #listen forever
    data, clientAddress = serverSocket.recvfrom(2048) #When a packet arrives the packet’s data is put into "modifiedMessage"                                                     #and the packet’s source address is put into "serverAddress", recvfrom
    message = data.decode()                                                    #takes the buffer size 2048 as input
    print("Recieved message from {}: {}".format(clientAddress[0],message))
    clients.add(clientAddress[0])

    print("Server Test Server")
    i = 1
    for client_address in clients:
        print("{}- Recieved message from {} at {}".format(i,client_address,time.ctime()))
        i += 1