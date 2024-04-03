#!/usr/bin/env python3
"""
1-fifo_cache.py
"""
from basecaching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        self.first_item = None
        super().__init__()
    def put(self, key, item):
        if len(self.cache_data) >= self.MAX_ITEMS:
            del self.cache_data.get(self.first_item)
            print("DISCARD: ", self.first_item)
        if not self.cache_data.get(key):
            self.first_item = key
        return super().put(key, item)