#!/usr/bin/env python3

"""
A type-annotated function that takes a float 'multiplier'
returns a function that multiplies a float by 'mu;tiplier'.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by 'multiplier'
    """

    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function


# Tests
# make_multiplier = __import__('8-make_multiplier').make_multiplier
# print(make_multiplier.__annotations__)
# fun = make_multiplier(2.22)
# print("{}".format(fun(2.22)))
