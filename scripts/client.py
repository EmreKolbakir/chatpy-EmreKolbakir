import socket
import threading

nickname = input("Choose your nickname: ")

# Create the client socket that will use IPv4 and TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client socket to the server. Make sure the server is running on this IP address and port.
client.connect(('127.0.0.1', 8765))

# Function to handle receiving messages from the server.
def receive():
    while True:
        try:
            # 'ascii' decoding is used to convert bytes to a human-readable string.
            message = client.recv(1024).decode('ascii')

            # If 'NICK' command is received, send the nickname to the server.
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                # If any other message is received, print it to the console.
                print(message)
        except:
            # If any error occurs (like server closing), close the client socket and exit the loop (end the thread).
            print("An error occurred!")
            client.close()
            break

# Function to continuously prompt the user for input (messages to send to the chat).
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

# Create and start the receiving thread. Upon starting, it calls the 'receive' function.
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Create and start the writing thread. Upon starting, it calls the 'write' function.
write_thread = threading.Thread(target=write)
write_thread.start()
