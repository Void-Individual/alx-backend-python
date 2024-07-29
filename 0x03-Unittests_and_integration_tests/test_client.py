#!/usr/bin/env python3
"""Test module for the client module"""

import unittest
from unittest.mock import patch
from client import (GithubOrgClient)
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Class to test the client module"""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    def test_org(self, org_name, test_payload):
        """Test that GithubOrgClient.org returns the correct value"""

        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()

        github_client = GithubOrgClient(org_name)
        github_client.org
        mock.assert_called_once()
        patcher.stop()

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url for expected result"""

        config = {'return_value.json.return_value': {"repos_url": True}}
        patcher = patch('requests.get', **config)
        mock = patcher.start()

        github_client = GithubOrgClient("org_name")
        github_client._public_repos_url
        mock.assert_called_once()
        patcher.stop()
