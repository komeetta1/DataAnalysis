from math import hypot

"""Data analysis with python usemodule tehtävä"""
def hypothenuse(num1, num2):
    """returns the length of the hypothenuse when given the lengths of two other sides of a right-angled triangle"""
    x = hypot(num1, num2)
    return x

def area(side1, side2):
    """returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters"""
    x = 0.5 * side1 * side2
    return x