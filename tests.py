# 362A2TDD


import unittest 
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
    
    def test1(self):
        input = 12345678 
        expected ='12345678'
        self.assertFalse(check_pwd(input), expected)



if __name__ == '__main__':
    unittest.main()

