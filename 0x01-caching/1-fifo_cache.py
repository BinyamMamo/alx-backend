#!/usr/bin/env python3
"""
Task 1. FIFO caching
Create a class `FIFOCache` that inherits from `BaseCaching`
and implements FIFO (First In, First Out) caching algorithm.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Implements a FIFO caching strategy using a deque to track order.
    """

    def __init__(self):
        """Initialize the FIFOCache."""
        from collections import deque
        self.queue = deque()
        super().__init__()

    def get(self, key):
        """Get an item from the cache.
        """
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """Put an item into the cache.
        """
        if len(self.cache_data) >= self.MAX_ITEMS:
            first_item = self.queue[0]
            del self.cache_data.get(first_item)
            self.queue.popleft()
            print("DISCARD: ", first_item)
        if not self.cache_data.get(key, None):
            self.queue.append(key)

        self.cache_data[key]= item
