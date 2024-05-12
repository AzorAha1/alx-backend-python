#!/usr/bin/env python3
"""unittest

Keyword arguments:
argument -- description
Return: return_description
"""


import unittest
import parameterized
from utils import access_nested_map
from typing import Any, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """unitties

    Args:
        unittest (_type_): _description_
    """
    @parameterized.parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected) -> Any:
        """test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
