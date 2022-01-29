import requests

url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=0200108"

response = requests.get(url)
print(response.text)
