#!/usr/bin/env python3

"""
A function named 'index_range' that takes two integer arguments
'page' and 'page_size'

The function returns a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters

Page numbers are 1-indexed. ie. the first page is page 1
"""

import csv
import math
from typing import List, Union


def index_range(page: int, page_size: int) -> List[int]:
    """
    Returns a tuple of size two
    """

    start_index = page - 1
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(
        self,
        page: int = 1,
        page_size: int = 10) -> Union[List[List],
                                      Exception]:

        try:
            result = index_range(page, page_size)
            dataset_size = len(self.dataset())

            if (result[1] > dataset_size):
                return []
            else:
                return self.dataset()[result[0]:result[1]]
        except TypeError:
            return AssertionError


# Tests
# server = Server()

# try:
#     should_err = server.get_page(-10, 2)
# except AssertionError:
#     print("AssertionError raised with negative values")

# try:
#     should_err = server.get_page(0, 0)
# except AssertionError:
#     print("AssertionError raised with 0")

# try:
#     should_err = server.get_page(2, 'Bob')
# except AssertionError:
#     print("AssertionError raised when page and/or page_size are not ints")


# print(server.get_page(1, 3))
# print(server.get_page(3, 2))
# print(server.get_page(3000, 100))
# print(server.get_page(19400, 100))
