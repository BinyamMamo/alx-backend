#!/usr/bin/env python3
"""
Task 0. Simple helper function
Write a function named `index_range` that
takes two integer arguments `page` and `page_size`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the start and end index for a given page and page size.

    Args:
        page (int): The page number, 1-indexed
        page_size (int): The number of items per page

    Returns:
        Tuple[int, int]: The start and end index as a tuple
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
