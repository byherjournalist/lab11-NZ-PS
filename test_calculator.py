import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(-4, -6), -10)

    def test_subtract(self):
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(4, 10), -6)
        self.assertEqual(sub(-5, -3), -2)

    def test_divide_by_zero(self):
        # Remember: div(a, b) computes b / a, so a = 0 triggers ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        # Remember: log(a, b) computes log base a of b
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(3, 9), 2.0)

    def test_log_invalid_base(self):
        # Base <= 0 or base == 1 should raise ValueError
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(0, 10)
        with self.assertRaises(ValueError):
            log(-2, 10)
