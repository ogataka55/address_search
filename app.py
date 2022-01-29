import requests


def search_address(zipcode):
    url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    response = requests.get(url)
    results = response.json()['results']
    print(response.json())
    pref_name = results[0]['address1']
    city_name = results[0]['address2']
    town_name = results[0]['address3']
    address = f"{pref_name}{city_name}{town_name}"
    return address


def main():
    zipcode = "0287111"
    # zipcode = input("郵便番号<ハイフン無し7桁は>？")

    address = search_address(zipcode=zipcode)
    print(address)


if __name__ == '__main__':
    main()
