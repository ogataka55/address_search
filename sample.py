from search_address import search_address


def main():
    zipcode = "0200108"

    address = search_address(zipcode)

    assert "岩手県盛岡市東黒石野" == address


if __name__ == '__main__':
    main()
