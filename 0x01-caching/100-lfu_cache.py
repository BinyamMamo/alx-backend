#!/usr/bin/env python3
"""
Task 5. LFU Caching (#advanced)
Module implementing a Least Frequently Used (LFU) cache.

Classes:
    LFUCache - LFU cache implementation inheriting from BaseCaching.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache implementation.

    Implements a Least Frequently Used cache that discards the least frequently
    used item first when the cache is full and a new item needs to be inserted.

    Attributes:
        cache_data (OrderedDict): Dictionary to store cache data, ordered by
            frequency of use.
        keys_freq (list): List of key-frequency tuples
            tracking frequency of use
    """

    def __init__(self):
        """Initializes the LFU cache.

        Calls the parent class __init__ method to initialize cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """Reorders items in frequency list when key accessed.

        Pops the key from current position and inserts it back at correct
        position based on new frequency count.

        Args:
            mru_key: The most recently used key that needs to be reordered.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """Inserts or updates item in cache.
        Implements cache insertion and overflow logic. If key not present,
        inserts item. If present, updates value and reorders frequency.
        If overflow, removes least frequently used item before insertion.

        Args:
            key: Key of item to insert or update
            item: Value of item to insert or update
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves item from cache.

        If key is in cache, returns value and reorders frequency.
        Otherwise returns None.

        Args:
            key: Key of item to retrieve

        Returns:
            Value of item if key is in cache, else None
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
