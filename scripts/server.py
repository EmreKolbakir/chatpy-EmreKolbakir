import socket
import threading

host = '127.0.0.1'  # Localhost IP. The server is reachable only on the same machine.
port = 8765

# Create a socket instance to enable connections.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to a specific IP and port combination. It starts listening for connections on this address.
server.bind((host, port))
server.listen()

# Lists to store active clients and their corresponding nicknames for easy management and communication broadcasting.
clients = []
nicknames = []

# Function to broadcast a message to all connected clients.
def broadcast(message):
    for client in clients:
        client.send(message)

# Function that handles incoming messages from clients, broadcasting them to the entire chatroom.
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # If a client disconnects or an error occurs, remove the client and close the connection.
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

# Main function to receive and manage incoming client connections.
def receive():
    while True:
        # Accept a connection request from a client.
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Request the client's nickname and store it.
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Inform all connected clients of the new client.
        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start a new thread to handle the client's incoming messages.
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Start the server's main loop.
print("Server is listening...")
receive()
