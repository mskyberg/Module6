"""
Program: validate_input_in_functions.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: To demonstrate validating input
"""


def score_input(test_name, test_score=0,
                invalid_message='Invalid test score, try again!'):
    """
    Function to validate a test score

    :param test_name: the name of the test
    :param test_score: the score to be validated
    :param invalid_message: the message presented if input is invalid
    :returns: key value pair of test name, score or invalid message
    :raises TypeError: raises an exception with non-numeric input
    """
    try:
        if test_score < 0 or test_score > 100:
            return invalid_message
    except TypeError as err:
        print(f'Type error: {err}')
        return invalid_message
    else:
        return {test_name: test_score}


if __name__ == '__main__':
    print(score_input('MainTest1', 90))
    print(score_input('MainTest2', 'CAT', 'Well, Shoot'))
