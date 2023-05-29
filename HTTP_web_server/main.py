import os
from socket import *

server_name = "192.168.0.174"
server_port = 9977
listening_socket = socket(AF_INET, SOCK_STREAM)  # Creates a TCP socket for incoming requests
listening_socket.bind((server_name, server_port))  # Assigns the host name (IP address) & port number to the server’s socket
listening_socket.listen(1)  # The server listens for TCP connection requests from clients with 1 queued connection.
print("---------------------------------------------------")
print("* The web server is ready to receive HTTP requests.")
print("---------------------------------------------------")


def not_found(ip, port):
    dedicated_socket.send("HTTP/1.1 404 Not Found \r\n".encode())  # in this case, the server sends a 404 Not Found HTTP response to the client
    dedicated_socket.send("Content-Type: text/html \r\n".encode())  # type text HTML
    dedicated_socket.send(
        "\r\n".encode())  # HTML document containing a message indicating that the requested resource was not found
    # includes information about our team's names and IDs ALSO IP and port of the server.
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
    # if the request is wrong or the file doesn’t exist the server should return a simple HTML webpage that contains with
    not_found_html_bytes = bytes(not_found_html, "UTF-8")
    dedicated_socket.send(not_found_html_bytes)


while True:
    dedicated_socket, client_ip_and_port = listening_socket.accept()  # When a client sends a TCP connection request create a socket dedicated to this client
    HTTP_request = dedicated_socket.recv(2048).decode()
    print("------------------------------------------------------------------------------------------------")
    object_URL = HTTP_request.split(" ")[1]  # Get URL of requested resource (e.g. default HTTP request starts with "GET / HTTP/1.1").
    print(f"** Serving client with IP ({client_ip_and_port[0]}) & port ({client_ip_and_port[1]}) with the following HTTP request of ({object_URL}):-")
    print("------------------------------------------------------------------------------------------------")
    print(HTTP_request)
    print("------------------------------------------------------------------------------------------------")

    if object_URL == '/' or object_URL == '/index.html' or object_URL == '/main_en.html' or object_URL == '/en':  # Serving English main page file
        print(os.path)
        if os.path.exists("../") or os.path.exists("./index.html") or os.path.exists(
                "main_en.html") or os.path.exists("./en"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: text/html\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open("main_en.html", "rb")
            dedicated_socket.send(file.read())
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL == '/ar':  # Serving Arabic main page file
        if os.path.exists("main_ar.html"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: text/html\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open("main_ar.html", "rb")
            dedicated_socket.send(file.read())
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL.endswith('.html'):  # Serving a specific HTML file other than main page file
        if os.path.exists(f"./{object_URL}"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: text/html\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open(f"./{object_URL}", "rb")
            dedicated_socket.send(file.read())
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL.endswith('.css'):
        if os.path.exists(f"./{object_URL}"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: text/css\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open(f"./{object_URL}", "rb")
            dedicated_socket.send(file.read())
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL.endswith('.png'):
        if os.path.exists(f"./{object_URL}"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: image/png\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open(f"./{object_URL}", "rb")
            dedicated_socket.send(file.read())
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL.endswith('.jpg'):
        if os.path.exists(f"./{object_URL}"):
            dedicated_socket.send("HTTP/1.1 200 OK\r\n".encode())
            dedicated_socket.send("Content-Type: image/jpeg\r\n".encode())
            dedicated_socket.send("\r\n".encode())
            file = open(f"./{object_URL}", "rb")
            dedicated_socket.send(file.read())
        else:
            not_found(client_ip_and_port[0], client_ip_and_port[1])

    elif object_URL == '/yt' or object_URL == '/so' or object_URL == '/rt':  # If the request is for '/yt', 'so', or 'rt', the server sends a 307 Temporary Redirect HTTP response to the client instructing the client to make a new request to the specified URL in the Location header.
        dedicated_socket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        dedicated_socket.send("Content-Type: text/html\r\n".encode())
        if object_URL == '/yt':
            location_header = "Location: https://www.youtube.com\r\n"
        elif object_URL == '/so':
            location_header = "Location: https://stackoverflow.com\r\n"
        elif object_URL == '/rt':
            location_header = "Location: https://ritaj.birzeit.edu\r\n"
        dedicated_socket.send(location_header.encode())
        dedicated_socket.send("\r\n".encode())
        dedicated_socket.close()  # close the connection since user is going to different website

    else:  # Requested resource type not supported
        not_found(client_ip_and_port[0], client_ip_and_port[1])

    if HTTP_request.__contains__("Connection: close\r\n"):  # Persistent connection until last request asks to close the socket connection.
        dedicated_socket.close()  # close the connection
