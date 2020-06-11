"""
Program: string_functions.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: to demonstrate the use of parameters in a function
"""


def multiply_string(message, n):
    """
    Description: this function multiplies a string

    :param message: string to multiply
    :param n: number of times to multiply string
    :returns: new string multiplied by n
    """
    try:
        new_string = message * n
    except TypeError as e:
        print(f'Input error: {e}')
        raise TypeError
    else:
        return new_string


if __name__ == '__main__':
    try:
        print(multiply_string('Python!', 6))
        print(multiply_string('Python!', 'Python'))
    except TypeError:
        print('Input Error')
