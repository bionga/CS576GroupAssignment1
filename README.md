# TCP Socket
TCP server and TCP client connects and communicates with each other.

## Description
TCP server accepts connection and receives a string from a client that is 256 characters 
or less. This message is converted to a new message by replacing each character with the
next character in the ASCII sequence. This encoded message is sent back to the client and
outputted.  
A TCP server is created, binded to an IP and port, then listens for connections and their 
messages. Received messages has each character shifted one ASCII character up, then sends the
new message back to the client address. There is error checking within every step.  
A TCP client is also created, binded to the same IP address and port, then attempts to send a 
message to the server. If a message is received back, it is then printed.

## Authors
CS 576 Group 1
- Alyssa Biong
- Gershom Delgado
- Cassie Scott
- Patricia Morales Alfonso
- Noah Tsi Meng Thao
- Katelyn Tamayo Nguyen
- Zobair Staneksay
- Anirudh Jha
