import requests

url = "https://google.com"

response  = requests.get(url, timeout=20)
html = response.text
print(html[:300])