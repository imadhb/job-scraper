import requests
from bs4 import BeautifulSoup
url = "https://google.com"

response  = requests.get(url, timeout=20)
html = response.text
soup = BeautifulSoup(html, "html.parser")
a_tags = soup.find_all("a")
print("Number of <a> tags:", len(a_tags))
print("Type of <a> tags:", type(a_tags))
