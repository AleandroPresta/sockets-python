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

    # Check if the expected output is received
    assert "Example Domain" in printed_output  # Assuming "Example Domain" is part of the expected output

if __name__ == "__main__":
    pytest.main([__file__])
