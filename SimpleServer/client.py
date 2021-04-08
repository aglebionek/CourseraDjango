#%%
import socket
#remember the stuff about making phonecalls

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make a phone on your pc so you can call a server
try:
    my_socket.connect(('127.0.0.1', 8000)) # server domain, port to use (80 is basic http port)
except:
    print("server doesn't exist") # the socket.connect crashes if we dial a phone number that doesn't exist
command = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode('UTF-8') # first enter is to confirm the get command,
#we need to include the server, the protocol, and stuff like cookies etc which we don't have. Empty line confirms that we are not going to send anything else.l
#We also need to encode it - strings in python are in unicode, strings on web are utf8

my_socket.send(command) # we try to send the get command to the server we connected to

while True:
    data = my_socket.recv(512) # wait for 512 characters or if no more data is sent and the socket on the server's end is closed
    if len(data) < 1: break
    print(data.decode(), end='') # decode back to unicode

my_socket.close()
# %%
