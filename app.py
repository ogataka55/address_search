from search_address import search_address


def main():
    # zipcode = "0287111"
    zipcode = input("郵便番号<ハイフン無し7桁は>？")

    address = search_address(zipcode=zipcode)
    print(address)


if __name__ == '__main__':
    main()
