import socket
import sys

# define the socket location
HOST = '127.0.0.1' # localhost
PORT = 8088

# HTTP response sent to client
data = (
    "HTTP/1.1 200 OK"
    "Content-Type: text/html; charset=UTF-8\r\n"
    "\r\n"
    "<html>"
    "Congratulations! You've downloaded the first Wireshark lab file!"
    "</html>\r\n"
)

# create a socket
server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a given host and port
server_socket.bind((HOST, PORT))

# listen for incoming requests
server_socket.listen(1)
print(f"Server running on http://{HOST}:{PORT}/")

try:
    # the server always on
    while True:
        # accept an incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection received from {client_address}")

        # receive the client request, 1 KB at a time
        request = client_socket.recv(1024)
        print("Received request:\n", request.decode())

        # send HTTP response
        client_socket.sendall(data.encode())

        client_socket.close()
        print("Connection closed.\n")

except KeyboardInterrupt:
    # the user would like to close the connection
    print("\nShutting down server...")
    server_socket.close()
    sys.exit(0)