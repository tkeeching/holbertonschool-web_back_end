#!/usr/bin/env python3

"""
A type-annotated function that takes a float
argument and returns the string representation
of the float
"""


def to_str(n: float) -> str:
    """
    Returns the string representation of the float
    """
    return str(n)


# Tests
# pi_str = to_str(3.14)
# print(pi_str == str(3.14))
# print(to_str.__annotations__)
# print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
