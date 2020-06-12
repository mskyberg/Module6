"""
Program: inner_functions_assignment.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: demonstrate the use of inner functions
"""


def measurements(m_list):
    """
    calculate the area and perimeter of a rectangle or square
    :param m_list: list of length and width values
    :returns: string of calculated perimeter and area
    """

    def area(a_list):
        """
        calculate thea area
        :param a_list: list of length and width values
        :returns: calculated perimeter float
        """
        return a_list[0] * a_list[1]

    def perimeter(p_list):
        """
        calculate the perimeter
        :param p_list: list of length and width values
        :returns: calculated perimeter float
        """
        return 2 * (p_list[0] + p_list[1])

    # "Perimeter = 11.0 Area = 7.14"
    return f"Perimeter = {perimeter(m_list)} Area = {area(m_list)}"


if __name__ == '__main__':
    pass
