import urllib.request


def get_status(url):
    response = urllib.request.urlopen(url).getcode()
    return response

def is_url_valid(url):
    response = get_status(url)
    return response > 199 and response < 400;

