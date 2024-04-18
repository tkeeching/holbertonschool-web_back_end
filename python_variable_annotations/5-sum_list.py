#!/usr/bin/env python3

"""
A type-annotated function that takes a list
of floats as argument and returns their sum
as a float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum as a float
    """

    sum: float = 0.0

    for number in input_list:
        sum += number

    return sum


# Tests
# floats = [3.14, 1.11, 2.22]
# floats_sum = sum_list(floats)
# print(floats_sum == sum(floats))
# print(sum_list.__annotations__)
# print("sum_list(floats) returns {} which is a {}".format(
#     floats_sum, type(floats_sum)))
