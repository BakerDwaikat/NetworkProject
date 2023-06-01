from socket import *  # Import all functions from the socket library.
from datetime import datetime
from clients import *  # Import custom data object that stores a set of clients' info (IP, name, last_ping_time).
import netifaces as ni  # Import netifaces for pulling the subnet mask in order to calculate the broadcast address.

server_name = ni.ifaddresses(ni.gateways()["default"][2][1])[ni.AF_INET][0]['addr']  # Get the local host name (IP address) of this device.
SERVER_PORT = 8855  # Listen on this port.
server_socket = socket(AF_INET, SOCK_DGRAM)  # Create a socket with address family (IPv4) and socket type (UDP).
server_socket.bind((server_name, SERVER_PORT))  # Assign the host name (IP address) & port number to the server's socket.

print("-----------------------------------------------")
print("-----------------------------------------------")
print("Welcome to the UDP server. Please enter your:-")
first_name = input("First name: ")
last_name = input("Last name: ")
print("-------------------------------------------------")
print("-------------------------------------------------")
print("* SERVER INFO:")
print(f"  ** Owner: {first_name} {last_name}")
print(f"  ** Name (IP Address): {server_name}")
print(f"  ** Port #: {SERVER_PORT}")
print('  ** The server is ready to receive packets.')
print("-------------------------------------------------")
print("-------------------------------------------------")

clients = Clients()  # Custom data object that stores a set of clients' info (IP, name, last_ping_time).

while True:
    data, client_address = server_socket.recvfrom(2048)  # When a packet arrives the packet’s data (name of user in this case) and their IP are pulled from the buffer.
    message = data.decode('UTF-8')  # Decode and put the client's name in message.
    client_ip = client_address[0]  # Put the client's IP address into clientIP.
    current_time = datetime.now().strftime("%H:%M:%S")  # Get the current date & time in the specified format.
    clients.add_client(client_ip, message, current_time)  # Add the client's info to the clients set.

    print(f"Server {first_name} {last_name}")
    i = 1
    for client in clients:
        print(f"{i}- Received broadcast message from {client.get_name()} ({client.get_ip()}) at {client.get_time()}.")
        i += 1
    print("-------------------------------------------------")
client_socket.close()  # Even though unreachable (per project requirements I can't add more to the code for it to be reachable), it is necessary to close a socket after being done with it.
