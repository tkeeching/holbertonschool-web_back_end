#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10
                        ) -> Dict[str, Union[int, List[List]]]:
        """
        Returns a dictionary with the following key-value pairs:
          - 'index': the current start index of the return page.
                      That is the index of the first item in the current
                      page. For example if requesting page 3 with
                      'page_size' 20, and no data was removed from the
                      dataset, the current index should be 60.
          - 'next_index': the next index to query with. That should be
                          the index of the first item after the last item
                          on the current page.
          - 'page_size': the current page size
          - 'data': the actual page of the dataset
        """

        dataset = self.dataset()
        assert isinstance(index, int) and index < len(dataset)

        result = {}
        end_index = index + page_size
        data = dataset[index:end_index]

        result['index'] = index
        result['next_index'] = end_index if end_index < len(dataset) else None
        result['page_size'] = len(data)
        result['data'] = data

        return result


# Tests
# server = Server()

# server.indexed_dataset()

# try:
#     server.get_hyper_index(300000, 100)
# except AssertionError:
#     print("AssertionError raised when out of range")


# index = 3
# page_size = 2

# print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# # # 1- request first index
# res = server.get_hyper_index(index, page_size)
# print(res)

# # # 2- request next index
# print(server.get_hyper_index(res.get('next_index'), page_size))

# # # 3- remove the first index
# del server._Server__indexed_dataset[res.get('index')]
# print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# # # 4- request again the initial index -> the first data retreives is
# # # not the same as the first request
# print(server.get_hyper_index(index, page_size))

# # # 5- request again initial next index -> same data page as the request 2-
# print(server.get_hyper_index(res.get('next_index'), page_size))
