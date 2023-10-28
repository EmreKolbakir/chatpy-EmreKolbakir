Introduction

ChatRoom is a lightweight chat application built using Python's socket and threading modules, 
creating a multi-threaded chat server that allows multiple clients to connect and communicate in real-time. 
This project aims to provide a fundamental understanding of how chat systems work, 
showcasing the interaction between servers and clients.

How to Use

1)Setup: Clone the repository to your local machine. Ensure you have Python installed.
2)Running the Server: Navigate to the directory containing 'server.py' and run the script using 
Python in your command line interface: python3 server.py

This will start the server, and it will listen for incoming connections.

3)Connecting as a Client: After starting the server, you can connect clients to the server. 
Open a new command line interface and navigate to the directory containing 'client.py'. 
Run the following command: python3 client.py
Enter your desired nickname when prompted.

4)Chatting: Repeat step 3 for each new client you want to connect. 
All connected clients can now communicate by typing messages into their command line interface.

5)Exiting the Chat: You can leave the chat session anytime by closing the client command line interface. 
The server will broadcast your departure to other clients.

Safety Concerns
While ChatRoom is a simplified demonstration of a chat system, it's essential to consider the following safety concerns:

No Encryption: Messages sent and received are not encrypted. 
They can potentially be intercepted and read by malicious parties.

Denial of Service Vulnerabilities: As a simple server, 
there's no implementation against DoS attacks, making it vulnerable.

No Authentication or Authorization: The system does not verify the identity of clients,
meaning anyone can connect using any nickname.

Data Safety: The server doesn't log chat sessions, 
but anyone with access to a client's command line can view the chat history.

It's recommended to use this application in a secure and trusted environment, primarily for learning purposes.
