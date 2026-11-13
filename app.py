
import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(20, 30), 50)

    def test_subtract(self):
        self.assertEqual(subtract(20, 15), 5)

    def test_multiply(self):
        self.assertEqual(multiply(7, 4), 28)


if __name__ == "__main__":
    print("Student Calculator Application")
    print("Addition:", add(20, 30))
    print("Subtraction:", subtract(20, 15))
    print("Multiplication:", multiply(7, 28))

    print("\nExecuting automated Tests...\n")

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
