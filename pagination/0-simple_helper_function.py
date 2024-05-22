#!/usr/bin/env python3

"""
A function named 'index_range' that takes two integer arguments
'page' and 'page_size'

The function returns a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters

Page numbers are 1-indexed. ie. the first page is page 1
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


# Tests
# res = index_range(1, 7)
# print(type(res))
# print(res)

# res = index_range(page=3, page_size=15)
# print(type(res))
# print(res)
