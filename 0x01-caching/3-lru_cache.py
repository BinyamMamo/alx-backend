#!/usr/bin/env python3
"""
Task 3. LRU Caching
Create a class `LRUCache` that inherits
from `BaseCaching` and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize LIFOCache instance"""
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache using the LIFO algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS \
                and key not in self.cache_data:
            first_item = self.queue[0]
            print("DISCARD: {}".format(first_item))
            del self.cache_data[first_item]
            del self.queue[0]

        if key in self.queue:
            del self.cache_data[key]

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache.
        """
        return self.cache_data.get(key, None)
