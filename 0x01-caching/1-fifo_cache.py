#!/usr/bin/env python3
"""
Task 1. FIFO caching
Create a class `FIFOCache` that inherits from `BaseCaching`
and implements FIFO (First In, First Out) caching algorithm.
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Implements a FIFO caching strategy using a deque to track order.
    """

    def __init__(self):
        """Initialize the FIFOCache."""
        self.queue = []
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Put an item into the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            first_item = self.queue[0]
            first_item = self.cache_data[first_item]
            print("DISCARD:", first_item)

            del self.cache_data[first_item]
            del self.queue[0]

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache.
        """
        return self.cache_data.get(key, None)
