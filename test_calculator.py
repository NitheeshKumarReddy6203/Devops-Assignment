import unittest
from calculator import add, subtract, multiply, lambda_handler

class TestCalculator(unittest.TestCase):
    # Test add function
    def test_add(self):
        result = add(2, 3)
        print(f"Addition result: {result}")
        self.assertEqual(result, 5)

    # Test subtract function
    def test_subtract(self):
        result = subtract(5, 3)
        print(f"Subtraction result: {result}")
        self.assertEqual(result, 2)

    # Test multiply function
    def test_multiply(self):
        result = multiply(2, 3)
        print(f"Multiplication result: {result}")
        self.assertEqual(result, 6)

    # Test lambda_handler for addition
    def test_lambda_handler_add(self):
        event = {"operation": "add", "a": 2, "b": 3}
        response = lambda_handler(event, None)
        print(f"Lambda addition response: {response}")
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["body"]["result"], 5)

    # Test lambda_handler for subtraction
    def test_lambda_handler_subtract(self):
        event = {"operation": "subtract", "a": 5, "b": 3}
        response = lambda_handler(event, None)
        print(f"Lambda subtraction response: {response}")
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["body"]["result"], 2)

    # Test lambda_handler for multiplication
    def test_lambda_handler_multiply(self):
        event = {"operation": "multiply", "a": 2, "b": 3}
        response = lambda_handler(event, None)
        print(f"Lambda multiplication response: {response}")
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["body"]["result"], 6)

    # Test lambda_handler for invalid operation
    def test_lambda_handler_invalid_operation(self):
        event = {"operation": "divide", "a": 6, "b": 3}
        response = lambda_handler(event, None)
        print(f"Lambda invalid operation response: {response}")
        self.assertEqual(response["statusCode"], 400)
        self.assertIn("Unsupported operation", response["body"])

    # Test lambda_handler for missing parameters
    def test_lambda_handler_missing_parameters(self):
        event = {"operation": "add", "a": 2}
        response = lambda_handler(event, None)
        print(f"Lambda missing parameters response: {response}")
        self.assertEqual(response["statusCode"], 400)
        self.assertIn("Missing required parameters", response["body"])

if __name__ == '__main__':
    unittest.main()
