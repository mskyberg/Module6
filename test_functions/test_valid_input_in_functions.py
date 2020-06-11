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
        self.assertEqual(validate.score_input('1stTest'), {'First Test': 0})

    def test_score_input_test_score_valid(self):
        self.assertEqual(validate.score_input('2ndTest', 90), {'2ndTest': 90})

    def test_score_input_test_score_below_range(self):
        self.assertEqual(validate.score_input('3rdTest', -1),
                         'Invalid test score, try again!')

    def test_score_input_test_score_below_range(self):
        self.assertEqual(validate.score_input('4thTest', 110),
                         'Invalid test score, try again!')

    def test_score_input_test_score_non_numeric(self):
        self.assertEqual(validate.score_input('5thTest', 'dog'),
                         'Invalid test score, try again!')

    def test_score_input_invalid_message(self):
        self.assertEqual(validate.score_input(
            '6thTest', 500, 'You\'re good but not that good, try again!'),
            'You\'re good but not that good, try again!')


if __name__ == '__main__':
    unittest.TestCase()
