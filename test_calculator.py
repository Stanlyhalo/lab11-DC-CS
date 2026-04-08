import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
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