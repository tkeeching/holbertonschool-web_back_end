#!/usr/bin/env python3

"""
A function named 'index_range' that takes two integer arguments
'page' and 'page_size'

The function returns a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters

Page numbers are 1-indexed. ie. the first page is page 1

Implement a 'get_hyper' method that takes the same arguments (and defaults)
as 'get_page' and returns a dictionary containing the following
key-value pairs:
  - 'page_size': the length of the returned dataset page
  - 'page': the current page number
  - 'data': the dataset page (equivalent to return from previous task)
  - 'next_page': number of the next page, 'None' if no next page
  - 'prev_page': number of the previous page, 'None' if no previous page
  - 'total_pages': the total nummber of pages in the dataset as an integer
"""

import csv
from typing import Tuple, List, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    Returns a tuple of size two
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve specified page
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset_size = len(self.dataset())

        if (end_index > dataset_size):
            return []
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10
                  ) -> Dict[int, Union[int, List[List]]]:
        """
        Returns a dictionary containing the following key-value pairs:
          - 'page_size': the length of the returned dataset page
          - 'page': the current page number
          - 'data': the dataset page (equivalent to return from previous
                    task)
          - 'next_page': number of the next page, 'None' if no next page
          - 'prev_page': number of the previous page, 'None' if no previous
                          page
          - 'total_pages': the total nummber of pages in the dataset as an
                            integer
        """

        result = {}

        data = self.get_page(page, page_size)

        start_index, end_index = index_range(page, page_size)
        dataset_size = len(self.dataset())

        if (end_index > dataset_size):
            result['page_size'] = 0
            result['next_page'] = None
        else:
            result['page_size'] = len(data)
            result['next_page'] = page + 1

        result['page'] = page
        result['data'] = data

        if (start_index == 0):
            result['prev_page'] = None
        else:
            result['prev_page'] = page - 1

        total_pages = (dataset_size + page_size - 1) // page_size
        result['total_pages'] = total_pages

        return result


# Tests
# server = Server()

# print(server.get_hyper(1, 2))
# print("---")
# print(server.get_hyper(2, 2))
# print("---")
# print(server.get_hyper(100, 3))
# print("---")
# print(server.get_hyper(3000, 100))
