#!/usr/bin/env python3
"""
Task 1. Simple pagination
"""
from typing import List, Tuple
import csv
import math


class Server:
    """
    Server class to paginate a database of popular baby names.
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
            assert isinstance(page, int), 'invalid data type'
            assert isinstance(page_size, int), 'invalid data type'
            assert page > 0, 'invalid page'
            assert page_size > 0, 'invalid page size'
            self.dataset()
            start_index, end_index = index_range(page, page_size)
            return self.__dataset[start_index: end_index]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the start and end index for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


if __name__ == "__main__":
    s = Server()
    s.dataset()