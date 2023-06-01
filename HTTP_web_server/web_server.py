import os
from socket import *

server_name = "127.0.0.1"  # Host this web server on this IP address (loopback address).
server_port = 9977  # Make this web server accessible through this port number.
listening_socket = socket(AF_INET, SOCK_STREAM)  # Create a socket with address family (IPv4) and socket type (TCP).
listening_socket.bind((server_name, server_port))  # Assign the host name (IP address) & port number to the server’s socket
listening_socket.listen(1)  # The server listens for TCP connection requests from clients with 1 queued connection allowed.
print("---------------------------------------------------")
print("* The web server is ready to receive HTTP requests.")
print("---------------------------------------------------")
DEFAULT_ENCODING = 'UTF-8'


# This function displays an error 404 (not found) webpage, indicating that the requested resource was not found, displaying the client's ip & port number on the webpage.
def not_found(ip, port):
    dedicated_socket.send("HTTP/1.1 404 Not Found \r\n".encode())
    dedicated_socket.send("Content-Type: text/html \r\n".encode())
    dedicated_socket.send("\r\n".encode())
    not_found_html = f"""<html>
                        <head>
                        <title>Error 404</title>
                        </head>
                        <body style='background-color: #f2f2f2;font-family: Arial, sans-serif;margin: 0;padding: 0;'>
                        <div style='display: flex;justify-content: center;align-items: center;height: 70vh;text-align: center;'>
                        <div style='font-size: 48px; font-weight: bold; color: red;'>Error 404 - The file is not found</div>
                        </div>
                        <div style='justify-content: center; align-items: center; height: 50vh; text-align: center;font-size: 24px;'>
                        <p style='font-weight: bold;'>Tala Maraaba - 1190126</p><br>
                        <p style='font-weight: bold;'>Baker Al-Sdeeq Dwaikat - 1192772</p><br/>
                        <p style='font-weight: bold;'>Ahmad Mtera - 1200607</p><br/>
                        </div>
                        <div style='justify-content: center; align-items: center; height: 50vh; text-align: center;font-size: 24px;'>
                        <p>Client IP: {ip}
                        </p></br>
                        <p>
                        Client Port #: {port}
                        </p>
                        </div>
                        </body>
                        </html>"""
    not_found_html_bytes = bytes(not_found_html, DEFAULT_ENCODING)  # Encode the webpage in the specified encoding.
    dedicated_socket.send(not_found_html_bytes)  # Send the webpage's bytes through the dedicated socket to the client.


while True:
    dedicated_socket, client_ip_and_port = listening_socket.accept()  # When a client sends a TCP connection request, create a socket dedicated to this client.
    HTTP_request = dedicated_socket.recv(2048).decode(DEFAULT_ENCODING)  # Decode the HTTP request received from the client and store it.
    if HTTP_request == "" or HTTP_request.split(" ").__len__() < 2:  # When the request is empty, show a message in the server's console.
        print("Empty request received. Nothing to do.")
        continue  # (Skip handling if received empty request).
    print("------------------------------------------------------------------------------------------------")
    object_URL = HTTP_request.split(" ")[1]  # Get the URL of the requested resource (e.g. default HTTP request starts with "GET / HTTP/1.1").
    print(f"** Serving client with IP ({client_ip_and_port[0]}) & port ({client_ip_and_port[1]}) with the following HTTP request of ({object_URL}):-")
    print("------------------------------------------------------------------------------------------------")
    print(HTTP_request)
    print("------------------------------------------------------------------------------------------------")

    if object_URL == '/' or object_URL == '/index.html' or object_URL == '/main_en.html' or object_URL == '/en':  # Serving English main page file
        if os.path.exists("./main_en.html"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: text/html\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open("./main_en.html", "rb")
            dedicated_socket.send(file.read())
            file.close()
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL == '/ar':  # Serving Arabic main page file
        if os.path.exists("./main_ar.html"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: text/html\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open("./main_ar.html", "rb")
            dedicated_socket.send(file.read())
            file.close()
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL.endswith('.html'):  # Serving a specific HTML file other than main page file
        if os.path.exists(f"./{object_URL}"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: text/html\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open(f"./{object_URL}", "rb")
            dedicated_socket.send(file.read())
            file.close()
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL.endswith('.css'):
        if os.path.exists(f"./{object_URL}"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: text/css\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open(f"./{object_URL}", "rb")
            dedicated_socket.send(file.read())
            file.close()
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL.endswith('.png'):
        if os.path.exists(f"./{object_URL}"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: image/png\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open(f"./{object_URL}", "rb")
            dedicated_socket.send(file.read())
            file.close()
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL.endswith('.jpg'):
        if os.path.exists(f"./{object_URL}"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: image/jpeg\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open(f"./{object_URL}", "rb")
            dedicated_socket.send(file.read())
            file.close()
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL == '/yt' or object_URL == '/so' or object_URL == '/rt':  # If the request is for '/yt', 'so', or 'rt', the server sends a 307 Temporary Redirect HTTP response to the client instructing the client to make a new request to the specified URL in the Location header.
        dedicated_socket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        dedicated_socket.send("Content-Type: text/html\r\n".encode())
        location_header = "Location: "
        if object_URL == '/yt':
            location_header = "Location: https://www.youtube.com\r\n"
        elif object_URL == '/so':
            location_header = "Location: https://stackoverflow.com\r\n"
        elif object_URL == '/rt':
            location_header = "Location: https://ritaj.birzeit.edu\r\n"
        dedicated_socket.send(location_header.encode())
        dedicated_socket.send("\r\n".encode())
        dedicated_socket.close()  # Close the connection since the user is going to a different website

    else:  # When the requested resource type is not supported.
        not_found(client_ip_and_port[0], client_ip_and_port[1])
    if HTTP_request.__contains__("Connection: close\r\n"):  # Keep socket open (Persistent Connection in HTTP/1.1) until a request asks to close the connection.
        dedicated_socket.close()  # Close the connection since the user requested that in the HTTP header.
