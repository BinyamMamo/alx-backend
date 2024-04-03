"""
Module containing unit tests for the FIFO cache.
"""
import unittest
from unittest.mock import patch
from typing import Tuple

FIFOCache = __import__('1-fifo_cache').FIFOCache


class TestFIFOCache(unittest.TestCase):
    """Class containing unit tests for the FIFOCache class."""

    @patch('1-fifo_cache.FIFOCache', autospec=True)
    def test_put_none_key(self, mock_cache):
        """Test putting a None key into the cache."""
        cache = FIFOCache()
        cache.put(None, 'value')
        mock_cache.put.assert_not_called()

    @patch('1-fifo_cache.FIFOCache', autospec=True)
    def test_put_none_value(self, mock_cache):
        """Test putting a None value into the cache."""
        cache = FIFOCache()
        cache.put('key', None)
        mock_cache.put.assert_not_called()

    def test_put_evicts_oldest_item(self):
        """Test that putting new items evicts the oldest item."""
        cache = FIFOCache()
        cache.put('1', 'one')
        cache.put('2', 'two')
        cache.put('3', 'three')

        self.assertEqual(cache.cache_data, {'2': 'two', '3': 'three'})

    def test_put_adds_new_item(self):
        """Test putting a new item into an empty cache."""
        cache = FIFOCache()
        cache.put('1', 'one')

        self.assertEqual(cache.cache_data, {'1': 'one'})
