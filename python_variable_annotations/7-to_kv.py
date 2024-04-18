#!/usr/bin/env python3

"""
A type-annotated function that takes a string 'k'
and an int OR float 'v' and returns a tuple.
The first element of the tuple is the string 'k'.
The second element is the square of the int/floar 'v'
and hsould be annotated as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of string and float
    """

    return (k, v*v)


# Tests
# print(to_kv.__annotations__)
# print(to_kv("eggs", 3))
# print(to_kv("school", 0.02))
