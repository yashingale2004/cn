import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Connect to server

# Send data to server
client_socket.send("Hello from the client!".encode('utf-8'))

# Receive response from server
data = client_socket.recv(1024).decode('utf-8')
print(f"Received from server: {data}")

# Close the connection
client_socket.close()