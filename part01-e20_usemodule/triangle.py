# Enter you module contents here
"""This module calculate the Hypothenuse and area of a right triangle"""
__author__ = "Kaysul"
__version__ = "1.0.0"

from math import sqrt


def hypothenuse(a, b):
    """This function calculates the Hypothenuse of a right triangle"""
    return sqrt(pow(a, 2) + pow(b, 2))


def area(a, b):
    """This function calculates the area of a isosceles triangle"""
    return (pow(a, 2))/2
