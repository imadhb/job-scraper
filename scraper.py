import requests
from bs4 import BeautifulSoup
url = "https://google.com"

response  = requests.get(url, timeout=20)
html = response.text
soup = BeautifulSoup(html, "html.parser")
print(type(soup))
