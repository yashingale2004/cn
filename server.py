import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # Bind to IP and port
server_socket.listen(5)  # Listen for connections
# new_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server is listening...")
# server_socket = socket.socket(socket.)
while True:
    client_socket, client_address = server_socket.accept()  # Accept connection
    print(f"Connection from {client_address}")
    print("Client connection successful")

    # Receive data from client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from client: {data}")

    # Send response to client
    client_socket.send("Hello from the server!".encode('utf-8'))

    # Close client connection
    client_socket.close()
    break
    # server_socket.close()

server_socket.close()
