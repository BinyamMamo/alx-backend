#!/usr/bin/env python3
"""
Task 0. Basic dictionary
Create a class `BasicCache` that inherits
from `BaseCaching` and is a caching system
"""
from basecaching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and implements get and put methods
    """

    def __init__(self) -> None:
        """
        Initialize the BasicCache object by calling the parent class __init__
        """
        super().__init__()

    def get(self, key):
        """
        Get an item from the cache by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """
        Add or update an item in the cache
        """
        if key or item:
            self.cache_data.update({key: item})
        pass
