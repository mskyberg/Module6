"""
Program: test_valid_input_in_functions.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Tests for validating input
"""


import unittest
from more_functions import validate_input_in_functions as validate


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(validate.score_input('First Test'), {'First Test': 0})


if __name__ == '__main__':
    unittest.TestCase()
