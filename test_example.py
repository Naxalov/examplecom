from main import get_h1_tag
import requests
# Write a test for the h1 tag
def test_get_h1_tag():
    # Get the website data
    URL = "https://www.example.com"
    data = requests.get(URL).text

    assert get_h1_tag(data) == "Example Domain"


