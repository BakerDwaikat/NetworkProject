from socket import *  # Import all functions from socket library

import time

print("Welcome to the UDP client. Please enter your:-")
first_name = input("First name: ")
last_name = input("Last name: ")
server_name = input("Server name (IP address): ")
SERVER_PORT = 8855
client_socket = socket(AF_INET, SOCK_DGRAM)
BROADCAST_INTERVAL = 2
message_template = "{} {}"

print("-------------------------------------------------")
print("-------------------------------------------------")


while True:
    message = message_template.format(first_name, last_name)
    client_socket.sendto(message.encode(), (server_name, SERVER_PORT))
    print(f"Broadcast message {message} sent to server {server_name}")
    time.sleep(BROADCAST_INTERVAL)
client_socket.close()  # While unreachable (per project requirements), it is necessary to close a socket after being done with it.

