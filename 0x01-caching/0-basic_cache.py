#!/usr/bin/env python3
"""
Task 0. Basic dictionary
Create a class `BasicCache` that inherits
from `BaseCaching` and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and implements get and put methods
    """

    def get(self, key: str) -> object:
        """
        Get an item from the cache by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)

    def put(self, key: str, item: object) -> None:
        """
        Add or update an item in the cache
        """
        if key and item:
            self.cache_data.update({key: item})
        pass
