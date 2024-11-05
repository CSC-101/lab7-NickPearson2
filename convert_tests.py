import unittest
import convert

class TestCases(unittest.TestCase):
    def test_str_to_float(self):
        self.assertEqual(convert.str_to_float("1.2"), 1.2)
        self.assertEqual(convert.str_to_float("Nice"), None)






if __name__ == '__main__':
    unittest.main()
