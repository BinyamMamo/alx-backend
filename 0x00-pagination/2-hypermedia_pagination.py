#!/usr/bin/env python3
"""
Task 1. Simple pagination
Implement a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10.
"""
from typing import List, Tuple
import csv


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
        """
        Gets a page from the dataset
        """
        assert isinstance(page, int), 'invalid data type'
        assert isinstance(page_size, int), 'invalid data type'
        assert page > 0, 'invalid page'
        assert page_size > 0, 'invalid page size'
        self.dataset()
        start_index, end_index = index_range(page, page_size)
        return self.__dataset[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data in hypermedia format
        """
        data = self.get_page(page, page_size)

        dtstlen = len(self.__dataset)
        start, end = index_range(page, page_size)
        prev_page = page - 1 if start - 1 in range(dtstlen) else None
        next_page = page + 1 if end + 1 in range(dtstlen) else None

        import math
        total_pages = math.ceil(dtstlen / page_size)

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the start and end index for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
