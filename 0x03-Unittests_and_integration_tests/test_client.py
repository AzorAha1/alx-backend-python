#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    @parameterized.expand([
        ('google', {'google': True}),
        ('abc', {'abc': True})
    ])
    @patch('client.get_json')
    def test_org(self, orgname, expected_response, mock_get):
        """sumary_line
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        mock_get.return_value = expected_response
        client = GithubOrgClient(orgname)
        org_result = client.org
        self.assertEqual(org_result, expected_response)
        mock_get.assert_called_once_with(
            f'https://api.github.com/orgs/{orgname}'
        )
