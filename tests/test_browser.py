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

    # Call the function to get the response
    response = perform_request(domain, port, url, request_type)

    # Check if the response contains the HTTP status code 200 OK
    assert 'HTTP/1.1 200 OK' in response

if __name__ == "__main__":
    pytest.main([__file__])
