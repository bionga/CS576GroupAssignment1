import socket

# create client TCP socket
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
# error message if socket creation fails
except socket.error as msg:
    print("Socket creation or connection error: " + str(msg))

# send test message
client.send('Hello World'.encode())

# display received message if received
data = client.recv(1024)
if data:
    print('Received from server: ' + data.decode())
else:
    print('No message received from server!')

client.close()