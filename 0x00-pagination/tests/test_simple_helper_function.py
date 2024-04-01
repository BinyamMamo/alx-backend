"""
Tests for index_range helper function.

Tests valid and invalid inputs and verifies correct start/end indexes are returned.
"""
import unittest

index_range = __import__('0-simple_helper_function').index_range


class TestIndexRange(unittest.TestCase):
    """Test the index_range helper function."""

    def test_valid_inputs(self):  
        """Test index_range with valid inputs."""
        start, end = index_range(1, 10)
        self.assertEqual(start, 0)
        self.assertEqual(end, 10)

    def test_invalid_page(self):
        """Test index range with invalid page."""
        start, end = index_range(0, 10)
        self.assertEqual(start, 0) 
        self.assertEqual(end, 0)


    def test_invalid_page_size(self):
        """
        Tests that index_range returns start=0 and
        end=0 when given an invalid page size of 0.
        """
        start, end = index_range(1, 0)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)

    def test_page_1_indexed(self):
        """
        Test that requesting page 1 returns
        the correct start and end indices.
        """
        start, end = index_range(1, 7)
        self.assertEqual(start, 0)
        self.assertEqual(end, 7)

    def test_page_not_1_indexed(self):
        """
        Test that index_range returns correct
        indices when page number is not 1-indexed.
        """
        start, end = index_range(3, 15)
        self.assertEqual(start, 30)
        self.assertEqual(end, 45)
