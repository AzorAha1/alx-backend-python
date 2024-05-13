#!/usr/bin/env python3
"""unittest
Keyword arguments:
argument -- description
Return: return_description
"""


import unittest
import unittest.mock
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map
from utils import get_json


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


class TestGetJson(unittest.TestCase):
    """_summary_
    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, expected_payload, mock_get):
        """test get json
        """
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = expected_payload
        mock_get.return_value = mock_response

        result = get_json(url)
        self.assertEqual(result, expected_payload)
