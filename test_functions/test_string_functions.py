"""
Program: test_string_functions.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: test the string functions for multiplying a string
"""

import unittest
from more_functions import string_functions as str_func


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual('MikeMikeMike', str_func.multiply_string('Mike', 3))
        self.assertEqual('AaAaAaAaAaAaAaAa', str_func.multiply_string('Aa', 8))

    def test_multiple_string_bad_type(self):
        with self.assertRaises(TypeError):
            str_func.multiply_string('Python!', 'Python!')


if __name__ == '__main__':
    unittest.TestCase()
