# list of all relevants tests for the project

from app.utils import *
from app.settings import SECRET_KEY


def test_utils_scrap_html_content():
    """
    This method will just tests the html scrapping feature of example.com

    """

    selector = "//div//h1"
    url = "http://example.com/"

    assert str(scrap_html_content(SECRET_KEY, selector, url)) == "<h1>Example Domain</h1>"

def test_utils_base64_encode():
    """
    A simple test methode for base64 encoding

    """
    assert b64_encode("test") == "dGVzdA=="

def test_utils_base64_decode():
    """
    A simple test methode for base64 decoding

    """
    assert b64_decode("dGVzdA==") == "test"
