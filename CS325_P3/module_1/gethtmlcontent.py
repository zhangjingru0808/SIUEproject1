import requests

def get_html_content(url):
    response = requests.get(url)
    return response.content.decode('utf-8')