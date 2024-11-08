import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-2, -4), -6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(9, 5), 4)
        self.assertEqual(self.calc.subtract(-1, 5), -6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 9), 9)
        self.assertEqual(self.calc.multiply(8, 2), 16) 

    def test_divide(self):
        self.assertEqual(self.calc.divide(20, 2), 10)
        self.assertEqual(self.calc.divide(15, 3), 5) 

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(9, 2), 1)
        self.assertEqual(self.calc.modulo(6, 3), 0)
        
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()