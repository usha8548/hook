import unittest

def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

class TestCalculator(unittest.Testcase):
  def test_add(self):
    self.assertEqual(add(20,20),40)
    
 def test_subtract(self):
    self.assertEqual(subtract(20,15),5)

 def test_multiply(self):
   self.assertEqual(multiply(3,4),12)

if __name__ == "__main__":
  print("student calculator application")
  print("Addition:",add(20,20))
  print("subtraction:",subtract(20,15))
  print("multiplication:",multiply(3,4))
  print("\nExecuting automated Tests...\n")
  unittest.main(argv=['first-arg-is-ignored'],exit=false)
