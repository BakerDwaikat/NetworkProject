import time
from socket import *

serverName = "192.168.1.10"
serverPort = 8855
clientSocket = socket(AF_INET, SOCK_DGRAM)
broadcast_interval = 2
MESSAGE_TEMPLATE = "{}"

while True:
    message = MESSAGE_TEMPLATE.format("Baker Al-Sdeeq Dwaikat")
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    print("Broadcast message sent:", message)

    time.sleep(broadcast_interval)
