import socket
from socket import *  # Import all functions from socket library
import netifaces as ni

import time

print("-----------------------------------------------")
print("-----------------------------------------------")
print("Welcome to the UDP client. Please enter your:-")
first_name = input("First name: ")
last_name = input("Last name: ")
client_IP = ni.ifaddresses(ni.gateways()["default"][2][1])[ni.AF_INET][0]['addr']  # Get the local host name (IP address) of this device
subnet_mask = ni.ifaddresses(ni.gateways()["default"][2][1])[ni.AF_INET][0]['netmask']  # Get the local host name (IP address) of this device
SERVER_PORT = 8855


def generate_broadcast_address(client_IP, subnet_mask):
    first_octet_client = int(client_IP.split(".")[0])
    second_octet_client = int(client_IP.split(".")[1])
    third_octet_client = int(client_IP.split(".")[2])
    fourth_octet_client = int(client_IP.split(".")[3])

    first_octet_mask = 255 - int(subnet_mask.split(".")[0])
    second_octet_mask = 255 - int(subnet_mask.split(".")[1])
    third_octet_mask = 255 - int(subnet_mask.split(".")[2])
    fourth_octet_mask = 255 - int(subnet_mask.split(".")[3])

    first_octet_broadcast = first_octet_client | first_octet_mask
    second_octet_broadcast = second_octet_client | second_octet_mask
    third_octet_broadcast = third_octet_client | third_octet_mask
    fourth_octet_broadcast = fourth_octet_client | fourth_octet_mask

    return str(first_octet_broadcast) + '.' + str(second_octet_broadcast) + '.' + str(third_octet_broadcast) + '.' + str(fourth_octet_broadcast)


broadcast_address = generate_broadcast_address(client_IP, subnet_mask)
print(f"Broadcasting to address: ({broadcast_address}) & port ({SERVER_PORT}).")


client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
BROADCAST_INTERVAL = 2
message_template = "{} {}"

print("---------------------------------------------------------")
print("---------------------------------------------------------")


while True:
    message = message_template.format(first_name, last_name)
    client_socket.sendto(message.encode(), (broadcast_address, SERVER_PORT))
    print(f"Broadcast message ({message}) sent.")
    time.sleep(BROADCAST_INTERVAL)
client_socket.close()  # While unreachable (per project requirements), it is necessary to close a socket after being done with it.

