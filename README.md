# HTTP Request Performer

This Python script enables users to perform HTTP requests to a specified domain and port, with a given URL and request type. It utilizes the `socket` module to establish a connection and send HTTP request commands, and subsequently displays the response received from the server.

## Script Explanation

- The script takes command line arguments for domain, port, URL, and request type.
- It establishes a socket connection to the specified domain and port.
- It constructs an HTTP request command based on the provided URL and request type.
- The script sends the request to the server and receives the response.
- The response is displayed to the user, including any HTTP headers and content.

## Usage

1. Clone or download the repository containing the `browser.py` script.
2. Navigate to the directory containing the script.
3. Run the script with the following command:

    ```
    python browser.py <domain> <port> <url> <request_type>
    ```

    Replace `<domain>`, `<port>`, `<url>`, and `<request_type>` with the desired values.
