import requests


def search_address(zipcode):
    if len(zipcode) != 7:
        return "郵便番号はハイフンなし7桁で入力してください"

    url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    response = requests.get(url)
    print(response.json())
    #  {'message': None,
    #  'results': [{'address1': '岩手県', 'address2': '盛岡市', 'address3': '東黒石野', 'kana1': 'ｲﾜﾃｹﾝ', 'kana2': 'ﾓﾘｵｶｼ',
    #  'kana3': 'ﾋｶﾞｼｸﾛｲｼﾉ', 'prefcode': '3', 'zipcode': '0200108'}], 'status': 200}
    results = response.json()['results']
    print(results)
    # [{'address1': '岩手県', 'address2': '盛岡市', 'address3': '東黒石野', 'kana1': 'ｲﾜﾃｹﾝ', 'kana2': 'ﾓﾘｵｶｼ', 'kana3': 'ﾋｶﾞｼｸﾛｲｼﾉ', 'prefcode': '3', 'zipcode': '0200108'}]

    # address = []
    # for index in range(len(results)):
    #
    #     pref_name = results[index]['address1']
    #     city_name = results[index]['address2']
    #     town_name = results[index]['address3']
    #     address.append(f"{pref_name}{city_name}{town_name}")
    #
    # return address

    addresses = []
    for result in results:
        pref_name = result['address1']
        city_name = result['address2']
        town_name = result['address3']
        addresses.append(f"{pref_name}{city_name}{town_name}")

    return addresses
