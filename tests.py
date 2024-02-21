# 362A2TDD


import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        input = 12345678
        expected = '12345678'
        self.assertTrue(check_pwd(input), expected)

    def test2(self):
        input = 1234567
        expected = '1234567'
        self.assertFalse(check_pwd(input), expected)

    def test3(self):
        input = 123456789123456789111
        expected = '123456789123456789111'
        self.assertFalse(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()
