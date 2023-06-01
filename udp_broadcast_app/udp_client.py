from socket import *  # Import all functions from the socket library.
import netifaces as ni  # Import netifaces for pulling the subnet mask in order to calculate the broadcast address.

import time

print("-----------------------------------------------")
print("-----------------------------------------------")
print("Welcome to the UDP client. Please enter your:-")
first_name = input("First name: ")
last_name = input("Last name: ")
client_IP = ni.ifaddresses(ni.gateways()["default"][2][1])[ni.AF_INET][0]['addr']  # Get the local host name (IP address) of this device.
subnet_mask = ni.ifaddresses(ni.gateways()["default"][2][1])[ni.AF_INET][0]['netmask']  # Get the local subnet mask of this device.
SERVER_PORT = 8855  # The broadcast message should be sent out to all host devices on the network that are listening to this port.
BROADCAST_INTERVAL = 2  # The message is retransmitted every number of seconds that this indicates.
message_template = "{} {}"


# This function receives the client's IP address and the network's subnet mask and returns the broadcast address.
# The broadcast address is calculated by executing the following function: Broadcast IP = (Any IP Address) | ~(Subnet Mask).
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


client_socket = socket(AF_INET, SOCK_DGRAM)  # Create a socket with address family (IPv4) and socket type (UDP).
client_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  # Set the socket type to a broadcast profile that allows the transmission of broadcast datagrams. 1 is the TTL since the packet only needs to pass into one router.

print("---------------------------------------------------------")
print("---------------------------------------------------------")


while True:
    message = message_template.format(first_name, last_name)  # Create the message: <Firstname> & <Lastname>
    client_socket.sendto(message.encode('UTF-8'), (broadcast_address, SERVER_PORT))  # Encodes and sends the message to the broadcast address and server port that's expected to listen for the packet.
    print(f"Broadcast message ({message}) sent.")
    time.sleep(BROADCAST_INTERVAL)
client_socket.close()  # Even though unreachable (per project requirements I can't add more to the code for it to be reachable), it is necessary to close a socket after being done with it.

