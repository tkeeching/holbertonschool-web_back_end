#!/usr/bin/env python3

"""
A type-annotated function that takes two
string arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Returns a concatenated string
    """
    return str1 + str2


# Tests
# str1 = "egg"
# str2 = "shell"

# print(concat(str1, str2) == "{}{}".format(str1, str2))
# print(concat.__annotations__)
