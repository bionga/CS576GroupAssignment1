import socket
import sys

# global variables
max_length = 256
host = '127.0.0.1'
port = 9999
s = None

# Create a socket (connecting two computers)
def create_socket():
    try:
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # error message if socket creation fails
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        
# Binding the socket and listening for connections
def bind_socket():
    try:
        print("Binding the Port: " + str(port))
        
        # Bind the socket to the host and port
        s.bind((host, port))
        # Listening for connections
        s.listen(5)

    # error message if binding fails
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()
        
# Establish connection with a client (socket must be listening)
def socket_accept():
    while True:
        conn, address = s.accept()  # constantly accept connections
        print("Connection has been established! | IP " + address[0] + " | Port" + str(address[1]))
        try:
            data = conn.recv(max_length)
            message = data.decode("ascii")
            if len(message) > max_length:
                # Error if message is too long
                print("Message is too long. Maximum length is " + str(max_length) + " characters.")
            else:
                encoded_message = ""
                for character in message:
                    # Encoding each character by shifting its ASCII value by 1
                    encoded_message += chr(ord(character) + 1) 
                response = "Encoded message: " + encoded_message
                conn.send(response.encode("ascii"))
                print("Received from client: " + message)
        except UnicodeDecodeError:
            # Error if message is not valid ASCII
            conn.send("Error: Received data is not valid ASCII.".encode())
        finally:
            conn.close()

# actually create server and convert client messages
create_socket()
bind_socket()
socket_accept()