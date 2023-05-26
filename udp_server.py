from socket import *  # Import all functions from socket library
from datetime import datetime
import netifaces as ni
from clients import *
import time as timer

serverSocket = socket(AF_INET, SOCK_DGRAM)  # Create a server socket with address family (IPv4) and socket type (UDP)
serverName = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']  # Get the local host name (IP address) of this device
serverPort = 8855
serverSocket.bind((serverName, serverPort))  # Assigns the host name (IP address) & port number 5566 to the server’s socket
broadcast_check_interval = 2
print("Welcome to the UDP server. Please enter your:-")
firstName = input("First name: ")
lastName = input("Last name: ")
print("-------------------------------------------------")
print("-------------------------------------------------")
print("* SERVER INFO:")
print(f"  ** Computer name: {firstName} {lastName}")
print("  ** Server name (IP Address): ", serverName)
print('  ** The server is ready to receive packets.')
print("-------------------------------------------------")
print("-------------------------------------------------")

clients = Clients()

while True:  # always listen
    data, clientAddress = serverSocket.recvfrom(2048)  # When a packet arrives the packet’s data (name of user in this case) and their IP are pulled from the buffer
    message = data.decode()  # put the client's name into message
    clientIP = clientAddress[0]  # put the client's address into clientIP
    time = datetime.now().strftime("%H:%M:%S")
    clients.add_client(clientIP, message, time)

    print(f"Server {firstName} {lastName}")
    i = 1
    for client in clients:
        print(f"{i}- Received broadcast message from {client.get_name()} ({client.get_ip()}) at {client.get_time()}.")
        i += 1
    print("-------------------------------------------------")
    timer.sleep(broadcast_check_interval)
