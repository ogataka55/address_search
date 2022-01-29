import unittest

from search_address import search_address


class MyTestCase(unittest.TestCase):
    def test_郵便番号0287302(self):
        actual = search_address("0287302")
        expected = [
            "岩手県八幡平市八幡平温泉郷",
            "岩手県八幡平市松尾寄木",
            "岩手県八幡平市松川温泉"]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
