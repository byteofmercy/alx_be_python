import unittest
from simple_calculator import add, subtract, multiply, divide

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

if __name__ == '__main__':
    unittest.main()
