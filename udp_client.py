from socket import *  # Import all functions from socket library

import time

print("Welcome to the UDP client. Please enter your:-")
firstName = input("First name: ")
lastName = input("Last name: ")
serverName = input("Server name (IP address): ")
serverPort = 8855
clientSocket = socket(AF_INET, SOCK_DGRAM)
broadcast_interval = 2
MESSAGE_TEMPLATE = "{} {}"

print("-------------------------------------------------")
print("-------------------------------------------------")


while True:
    message = MESSAGE_TEMPLATE.format(firstName, lastName)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    print(f"Broadcast message {message} sent to server {serverName}")

    time.sleep(broadcast_interval)
