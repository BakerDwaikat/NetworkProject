
from socket import *

serverPort=9977
serverSocket=socket(AF_INET,SOCK_STREAM) #creating a TCP socket for incoming request
serverSocket.bind(("",serverPort)) #associate the server port number "serverPort" with this socket
serverSocket.listen(1) #The server listen for TCP connection requests from the client with 1 queued connections.
print("The web server is ready to receive") #Print a message to tell the client that the server is ready to receive.
def NotFound():
    connectionSocket.send(
        "HTTP/1.1 404 Not Found \r\n".encode())  # in this case, the server sends a 404 Not Found HTTP response to the client
    connectionSocket.send("Content-Type: text/html \r\n".encode())  # type text HTML
    connectionSocket.send(
        "\r\n".encode())  # HTML document containing a message indicating that the requested resource was not found
    # includes information about our team's names and IDs ALSO IP and port of the server.
    notFoundHtmlString = "<html>" \
                         "<head>" \
                         "<title>Error 404 - Not Found</title>" \
                         "</head>" \
                         "<body style='background-color: #f2f2f2;font-family: Arial, sans-serif;margin: 0;padding: 0;'>" \
                         "<div style='display: flex;justify-content: center;align-items: center;height: 70vh;text-align: center;'>" \
                         "<div style='font-size: 48px; font-weight: bold; color: red;'>Error 404 - Not Found</div>" \
                         "</div>" \
                         "<div style='justify-content: center; align-items: center; height: 50vh; text-align: center;font-size: 24px;'>" \
                         "<p style='font-weight: bold;'>Tala Maraaba - 1190126</p><br>" \
                         "<p style='font-weight: bold;'>Baker Al-Sdeeq Dwaikat - 1192772</p><br/>" \
                         "<p style='font-weight: bold;'>Ahmad Mtera - 1200607</p><br/>" \
                         "</div>" \
                         "<div style='justify-content: center; align-items: center; height: 50vh; text-align: center;font-size: 24px;'>" \
                         f"<p>IP: {ip} " \
                         "</p></br>" \
                         "<p>" \
                         f"Port: {port}  " \
                         "</p>" \
                         "</div>" \
                         "</body>" \
                         "</html>"
    # if the request is wrong or the file doesn’t exist the server should return a simple HTML webpage that contains with
    notFoundHtmlBytes = bytes(notFoundHtmlString, "UTF-8")
    connectionSocket.send(notFoundHtmlBytes)

while True:
    connectionSocket, addr=serverSocket.accept() #When a client sends a TCP connection request create "connectionSocket" dedicated to this client
    sentence = connectionSocket.recv(2048).decode()
    print(addr)
    print(sentence)
    ip=addr[0]
    port=addr[1]
    object=sentence.split()[1]   #Get the reqested object from client request massage
    print(f"The HTTP request is: {object}")     #print the HTTP request on the terminal window

    if (object == '/' or object == '/index.html' or object == '/main_en.html' or object == '/en'): # The if statement checks whether the requested object is one of several specific values
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode()) #and if it is,it sends an HTTP response with a "200 OK" status code and the corresponding HTML file.
        connectionSocket.send("Content-Type: text/html \r\n".encode()) # send the HTML file: the content type "text/html"
        connectionSocket.send("\r\n".encode())
        file1=open("main_en.html", "rb") #then the server should send main_en.html file
        connectionSocket.send(file1.read()) #read the file that was open  when it called



    elif (object == '/ar'): #If object is equal to '/ar', it will send the same HTTP status code and content type,
        # but will serve the contents of the file "main_ar.html"
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        file2=open("main_ar.html", "rb")
        connectionSocket.send(file2.read())

    elif (object.endswith('.html')):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        file3=open(object[1:], "rb")
        connectionSocket.send(file3.read())
        print(object[1:])

    elif (object.endswith('.css')):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/css \r\n".encode())
        connectionSocket.send("\r\n".encode())
        file4 = open(object[1:], "rb")
        connectionSocket.send(file4.read())


    elif (object.endswith('.png')):
        flag = True
        try:
            file5 = open(object[1:], "rb")
        except FileNotFoundError as e:
            NotFound()
            flag = False
        if flag == True:
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: image/png \r\n".encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.send(file5.read())

    elif (object.endswith('.jpg')):
        flag = True
        try:
            file6 = open(object[1:], "rb")
        except FileNotFoundError as e:
            NotFound()
            flag = False
        if flag == True:
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.send(file6.read())

    elif (object == '/yt'): #status code 307 Temporary Redirect: If the request is for '/yt',
        # the server sends a 307 Temporary Redirect HTTP response to the client with
        # the Location header set to YOUTUBE
        # This instructs the client to make a new request to the specified URL.
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://www.youtube.com \r\n".encode())
        connectionSocket.send("\r\n".encode())

    elif (object == '/so'): #Similarly, if the request is for '/so', the server sends a 307 Temporary Redirect
        # HTTP response with the Location header set to 'https://stackoverflow.com',
        # instructing the client to make a new request to Stack Overflow.
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://stackoverflow.com \r\n".encode())
        connectionSocket.send("\r\n".encode())

    elif (object == '/rt'):#HTTP request that includes the string "/rt" in the URL. If this string is present.
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode()) #HTTP response to the client with a "307 Temporary Redirect" status code
        # and a "Location" header specifying that
        # the client should be redirected to the URL "https://www.birzeit.edu/en".This will cause the client's web browser to send a new request to the specified URL.
        connectionSocket.send("Content-Type: text/html \r\n".encode())#The response also includes a "Content-Type" header with a value of "text/html",
        # which indicates that the body of the response contains HTML content.
        connectionSocket.send("Location: https://www.ritaj.edu/en \r\n".encode())# HTTP response with the Location header set to birzeit edu
        connectionSocket.send("\r\n".encode())


    else: #scenario where a requested resource is not found by a client.
        NotFound()

    connectionSocket.close() #close the connection

