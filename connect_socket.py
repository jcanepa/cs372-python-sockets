import socket

# define server uri, port of recieving socket & route to file
host = 'gaia.cs.umass.edu'
port = 80
file = '/wireshark-labs/INTRO-wireshark-file1.html'

# create the socket
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM)

# connect to host at web server port
client_socket.connect(
    (host, port))

# build HTTP GET request
request = f"GET {file} HTTP/1.1\r\nHost:{host}\r\n\r\n"

# send request
client_socket.sendall(
    request.encode())

# accept a response from the server (as a byte literal)
response = b""
while True:
    chunk = client_socket.recv(4096)
    if not chunk:
        break
    # build response payload from chunks
    response += chunk

# close the socket
client_socket.close()

# print full response containing headers and content
print(response.decode(
    'utf-8'))