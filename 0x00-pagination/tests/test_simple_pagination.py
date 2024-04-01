import unittest
from unittest.mock import patch
from typing import Tuple

index_range = __import__('1-simple_pagination').index_range


class TestIndexRange(unittest.TestCase):

    def test_valid_inputs(self):
        start, end = index_range(1, 10)
        self.assertEqual(start, 0)
        self.assertEqual(end, 10)

    def test_zero_page_size(self):
        start, end = index_range(1, 0)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)

    def test_negative_page_size(self):
        start, end = index_range(1, -10)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)

    def test_string_page(self):
        with self.assertRaises(TypeError):
            start, end = index_range("1", 10)

    def test_string_page_size(self):
        with self.assertRaises(TypeError):
            start, end = index_range(1, "10")

    def test_float_page(self):
        with self.assertRaises(TypeError):
            start, end = index_range(1.5, 10)

    def test_float_page_size(self):
        with self.assertRaises(TypeError):
            start, end = index_range(1, 10.5)

    def test_zero_page(self):
        start, end = index_range(0, 10)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)

    def test_negative_page(self):
        start, end = index_range(-1, 10)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)
