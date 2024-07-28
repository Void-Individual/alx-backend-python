#!/usr/bin/env python3
"""Test module for the utils file"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """To inherit from a unittest method and check it"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, error):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(repr(context.exception), f"KeyError('{error}')")


class TestGetJson(unittest.TestCase):
    """Class to check the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, test_payload):
        """Test to confirm that the utils.get_json function returns
        the expected result"""

        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        result = get_json(url)

        # Test thata the get utput is equal to payload
        self.assertEqual(result, test_payload)
        # Test that the get method was called only once per input
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """Test class to affirm the memoize decorator"""

    def test_memoize(self):
        """Method to match the expected result of the memoize decorator"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            # mock_method.return_value = 42
            test_class = TestClass()
            result1 = test_class.a_property()
            result2 = test_class.a_property()
            # self.assertEqual(result1, 42)
            # self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
