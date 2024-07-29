#!/usr/bin/env python3
"""Test module for the client module"""

import unittest
from unittest.mock import patch, PropertyMock
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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test GithubOrgClient.public_repos to see if the list of
        repos is from the chosen payload"""

        # Init the instance
        payload = [{"name": "Test_name"}]
        mock_json.return_value = payload
        #patcher = patch('client.GithubOrgClient._public_repos_url', config)
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            mock.return_value = True
            github_client = GithubOrgClient("org_name")
            result = github_client.public_repos()
            expected = [key['name'] for key in payload]
            self.assertEqual(result, expected)

            mock.assert_called_once()
            mock_json.assert_called_once()
