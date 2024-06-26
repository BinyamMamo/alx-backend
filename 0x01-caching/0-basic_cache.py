#!/usr/bin/env python3
"""
Task 0. Basic dictionary
Create a class `BasicCache` that inherits
from `BaseCaching` and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and implements get and put methods
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Add or update an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
        pass

    def get(self, key):
        """
        Get an item from the cache by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
