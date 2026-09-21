import socket
import sys

# Create a socket (connecting two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = '127.0.0.1'
        port = 9999
        s = socket.socket()
    
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        
# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        
        print("Binding the Port: " + str(port))
        
        # Bind the socket to the host and port
        s.bind((host, port))
        # Listening for connections
        s.listen(5)
        
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()
        
# Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! | IP " + address[0] + " | Port" + str(address[1]))
    data = conn.recv(1024)
    print("Received from client: " + data.decode())
    conn.send('Hello Client!'.encode())
    conn.close()
            
def main():
    create_socket()
    bind_socket()
    socket_accept()

main()