#!/usr/bin/env python3

"""
A type-annotated function that takes two
float arguments and returns their sums
as a float
"""


def add(a: float, b: float) -> float:
    """
    Returns the sum as a float
    """
    return a + b


# Tests
# print(add(1.11, 2.22) == 1.11 + 2.22)
# print(add.__annotations__)
