"""
Program: test_inner_functions.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: test the inner function calculations
"""


import unittest
from more_functions import inner_functions_assignment as in_func


class MyTestCase(unittest.TestCase):
    def test_measurements_rectangle(self):
        self.assertEqual(in_func.measurements([2.1, 3.4]),
                         "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(in_func.measurements([3.5]),
                         "Perimeter = 14.0 Area = 12.25")


if __name__ == '__main__':
    unittest.TestCase()
