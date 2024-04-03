import socket
import sys

def perform_request(domain, port, url, request_type):
    # Create a socket object
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server using the provided domain and port
        mysock.connect((domain, port))

        # Define the HTTP request command with the provided URL and request type
        cmd = f'{request_type} http://{domain}{url} HTTP/1.0\r\n\r\n'.encode()

        # Send the request command to the server
        mysock.send(cmd)

        # Initialize an empty string to store the response
        response = ""

        # Receive data from the server in chunks of 512 bytes
        while True:
            data = mysock.recv(512)

            # Break the loop if no more data is received
            if len(data) < 1:
                break

            # Append the received data (decoded from bytes to string) to the response string
            response += data.decode()

        # Print the response
        print(response)

        # Return the response
        return response

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        # Close the socket connection
        mysock.close()

# Check if the script is being run directly
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python browser.py <domain> <port> <url> <request_type>")
        sys.exit(1)

    # Get command line arguments
    domain = sys.argv[1]
    port = int(sys.argv[2])
    url = sys.argv[3]
    request_type = sys.argv[4]

    # Call the function with the provided arguments
    perform_request(domain, port, url, request_type)
