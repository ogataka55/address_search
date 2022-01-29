import requests


def search_address(zipcode):
    url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    response = requests.get(url)
    results = response.json()['results']
    print(response)

    addresses = []
    for r in results:
        pref_name = r['address1']
        city_name = r['address2']
        town_name = r['address3']
        addresses.append(f"{pref_name}{city_name}{town_name}")
    return addresses
