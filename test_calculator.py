import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertAlmostEqual(add(1,3), 4)
        self.assertAlmostEqual(add(2,4), 6)
        self.assertAlmostEqual(add(6,8), 14)


    def test_subtract(self):
        self.assertAlmostEqual(subtract(8, 2), 6)
        self.assertAlmostEqual(subtract(10, 1), 9)
        self.assertAlmostEqual(subtract(2, 4), -2)
    # ##########################

    def test_multiply(self):
        self.assertAlmostEqual(mul(0, 1), 0)
        self.assertAlmostEqual(mul(-5, -5), 25)
        self.assertAlmostEqual(mul(5, -5), -25)

    def test_divide(self):
        self.assertAlmostEqual(div(10, 5), 0.5)
        self.assertAlmostEqual(div(5, 10), 2)
        self.assertAlmostEqual(div(0.2, 0.2), 1)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(100,10),2)
        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(125, 5), 3)



    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(5, -2)
    # ##########################

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))
        self.assertAlmostEqual(hypotenuse(4, 4), math.sqrt(32))
        self.assertAlmostEqual(hypotenuse(1, 5), math.sqrt(26))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(4), math.sqrt(4))

# Do not touch this
if __name__ == "__main__":
    unittest.main()