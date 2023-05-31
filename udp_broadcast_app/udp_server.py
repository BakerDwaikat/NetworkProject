from socket import *
from datetime import datetime
from clients import *
import netifaces as ni

server_name = ni.ifaddresses(ni.gateways()["default"][2][1])[ni.AF_INET][0]['addr']  # Get the local host name (IP address) of this device
SERVER_PORT = 8855
server_socket = socket(AF_INET, SOCK_DGRAM)  # Create a server socket with address family (IPv4) and socket type (UDP)
server_socket.bind((server_name, SERVER_PORT))  # Assigns the host name (IP address) & port number to the server’s socket
BROADCAST_INTERVAL = 2

print("-----------------------------------------------")
print("-----------------------------------------------")
print("Welcome to the UDP server. Please enter your:-")
first_name = input("First name: ")
last_name = input("Last name: ")
print("-------------------------------------------------")
print("-------------------------------------------------")
print("* SERVER INFO:")
print(f"  ** Owner: {first_name} {last_name}")
print("  ** Name (IP Address):", server_name)
print("  ** Port #:", SERVER_PORT)
print('  ** The server is ready to receive packets.')
print("-------------------------------------------------")
print("-------------------------------------------------")

clients = Clients()

while True:
    data, client_address = server_socket.recvfrom(2048)  # When a packet arrives the packet’s data (name of user in this case) and their IP are pulled from the buffer
    message = data.decode()  # Put the client's name into message
    client_ip = client_address[0]  # Put the client's IP address into clientIP
    current_time = datetime.now().strftime("%H:%M:%S")
    clients.add_client(client_ip, message, current_time)

    print(f"Server {first_name} {last_name}")
    i = 1
    for client in clients:
        print(f"{i}- Received broadcast message from {client.get_name()} ({client.get_ip()}) at {client.get_time()}.")
        i += 1
    print("-------------------------------------------------")
server_socket.close()  # While unreachable (per project requirements), it is necessary to close a socket after being done with it.
