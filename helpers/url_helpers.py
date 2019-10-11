import sys
import urllib.request
from urllib.error import *

def get_status(url):
    try:
        response = urllib.request.urlopen(url).getcode()
        return response
    except HTTPError as e:
        raise Exception(e.msg + "\nURL: " + url) from e

def is_url_valid(url):
    response = get_status(url)
    return response > 199 and response < 400;

