#!/usr/bin/env python3
"""Test module for the utils file"""

import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """To inherit from a unittest method and check it"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
