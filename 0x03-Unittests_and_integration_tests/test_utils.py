#!/usr/bin/env python3
"""unittest
Keyword arguments:
argument -- description
Return: return_description
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """unitties
    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_err):
        """_summary_

        Args:
            nested_map (_type_): _description_
            path (_type_): _description_
            expected_error (_type_): _description_
        """
        with self.assertRaises(expected_err):
            access_nested_map(nested_map, path)
