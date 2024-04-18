#!/usr/bin/env python3

"""
A type-annotated function that takes a float
argument and returns a concatenated string
"""


def floor(n: float) -> int:
    """
    Returns the floor of the float
    """
    return int(n)


# Tests
# import math

# ans = floor(3.14)

# print(ans == math.floor(3.14))
# print(floor.__annotations__)
# print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
