#%%
from socket import AF_INET, SOCK_STREAM, socket, SHUT_WR

def createServer():
    # create a phone
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # say that you are willing to answer phonecalls on port 9000
        serversocket.bind(('localhost', 8000))
        serversocket.listen(5) # listen for phonecalls and que up up to 4 additional get requests
        print('Server accessed at http://localhost:8000')
        while True:
            # if a connection is reqeuested, accept it
            (clientsocket, address) = serversocket.accept()

            # read what the client sent in it's get request
            rd = clientsocket.recv(5000).decode()
            rd = rd.split("\n")
            if rd: print(rd[0])

            # now lets create a response
            data = "HTTP/1.1 200 OK\r\n" # send the okay
            data += "Content-Type: text/html; charset=utf-8\r\n" # send info about document type (html)
            data += "\r\n" # empty line
            data += "<html><body>Hello World</body></html>\r\n\r\n" # html content

            # send the created response
            clientsocket.sendall(data.encode())
            # shut the connection after the data is sent
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt: # if we willingly turn the server off by keyboard interrupt
        print("\nShutting down...\n")
    except Exception as e: # catch any error that might occur
        print("Error:\n")
        print(e)

    # if we get here, that means we can close the server
    serversocket.close()

if __name__ == "__main__":
    createServer()


# %%
