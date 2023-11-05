# ChatterBox: A Simple Chat Server and Client in Python 📬👥

Welcome to **ChatterBox**! This is a Python-based chat application that allows multiple users to connect to a chatroom and communicate with each other in real-time. Utilizing the power of Python's `socket` and `threading` libraries, this application provides a simple yet functional example of a client-server architecture for a text-based group chat.

## Features 🌟

- Real-time text messaging between users.
- Concurrent handling of multiple client connections.
- Simple and intuitive command-line interface.
- Easy-to-setup server and client scripts.

## How It Works 🛠️

- The **Server** script sets up a listening socket and waits for clients to connect. Once a client connects, it handles incoming messages and broadcasts them to all other connected clients.
- The **Client** script connects to the server, enabling the user to join the chatroom. Users can send and receive messages from others in real-time.

## Getting Started 🚀

### Prerequisites

- Python 3.x installed on your machine.

### Setting Up the Server

1. Clone the repository:

git clone https://github.com/[YourUsername]/chatpy.git

2. Navigate to the project directory:

cd ChatterBox

3. Run the server script:

python server.py


### Connecting with the Client

1. Open a new command-line interface.
2. Run the client script:

python client.py

3. When prompted, enter a nickname of your choice.

### Engaging in Chat

- Type your message into the console to chat.
- Your message will be visible to all users connected to the chatroom.

## Dependencies 📦

- Python 3.x
- No external libraries are required.

## Safety Concerns 🔒

While this chat application is great for understanding the basics of network programming and client-server communication, it's not encrypted and should not be used to exchange sensitive information. Use it responsibly within a secure and trusted network environment.



