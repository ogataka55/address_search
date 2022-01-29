import requests

zipcode = "0287111"
# zipcode = input("郵便番号<ハイフン無し7桁は>？")

url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

response = requests.get(url)
print(response.text)
