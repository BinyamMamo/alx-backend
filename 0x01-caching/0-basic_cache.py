#!/usr/bin/env python3
"""
Task 0. Basic dictionary
Create a class `BasicCache` that inherits
from `BaseCaching` and is a caching system
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class")


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
