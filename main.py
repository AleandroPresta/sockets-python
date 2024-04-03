import socket  # Import the socket module

# Create a socket object
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server 'data.pr4e.org' on port 80
mysock.connect(('data.pr4e.org', 80))

# Define the HTTP GET request command with the desired URL
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# Send the GET request command to the server
mysock.send(cmd)

# Receive data from the server in chunks of 512 bytes
while True:
    data = mysock.recv(512)

    # Break the loop if no more data is received
    if len(data) < 1:
        break

    # Print the received data (decoded from bytes to string) without adding a newline
    print(data.decode(), end='')

# Close the socket connection
mysock.close()
