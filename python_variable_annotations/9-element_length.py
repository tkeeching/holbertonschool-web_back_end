#!/usr/bin/env python3

"""
Duck type an iterable object
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuple
    """

    return [(i, len(i)) for i in lst]


# Tests
# print(element_length.__annotations__)
