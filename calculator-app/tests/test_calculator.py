import unittest
from src.calculator import add, subtract, multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        print(f"Addition result: {result}")
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = subtract(5, 3)
        print(f"Subtraction result: {result}")
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = multiply(2, 3)
        print(f"Multiplication result: {result}")
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
