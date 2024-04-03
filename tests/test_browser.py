import sys
import os
# Add the parent directory of src to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.browser import perform_request

def test_perform_request():
    # Define test parameters
    domain = 'data.pr4e.org'
    port = 80
    url = '/page1.htm'
    request_type = 'GET'

    # Redirect stdout to capture print statements
    import sys
    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the function
    perform_request(domain, port, url, request_type)

    # Get the printed output
    printed_output = captured_output.getvalue()

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Defining the expected result
    expectedResult = 'HTTP/1.1 200 OK\nDate: Wed, 03 Apr 2024 17:34:34 GMT\nServer: Apache/2.4.52 (Ubuntu)\nLast-Modified: Mon, 15 May 2017 11:11:47 GMT\nETag: "80-54f8e1f004857"\nAccept-Ranges: bytes\nContent-Length: 128\nCache-Control: max-age=0, no-cache, no-store, must-revalidate\nPragma: no-cache\nExpires: Wed, 11 Jan 1984 05:00:00 GMT\nConnection: close\nContent-Type: text/html\n<h1>The First Page</h1>\n<p>\nIf you like, you can switch to the \n<a href="http://data.pr4e.org/page2.htm">\nSecond Page</a>.\n</p>'

    # Check if the expected output is received
    assert expectedResult in printed_output  # Assuming "Example Domain" is part of the expected output

if __name__ == "__main__":
    pytest.main([__file__])
