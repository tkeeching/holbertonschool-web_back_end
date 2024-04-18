#!/usr/bin/env python3

"""
A type-annotated function that takes a list
of integers and floats and returns their sum
as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns the sum as a float
    """

    return sum(mxd_list)


# Tests
# print(sum_mixed_list.__annotations__)
# mixed = [5, 4, 3.14, 666, 0.99]
# ans = sum_mixed_list(mixed)
# print(ans == sum(mixed))
# print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
