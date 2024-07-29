#!/usr/bin/env python3
"""Test module for the client module"""

import unittest
from unittest.mock import patch, PropertyMock
from client import (GithubOrgClient)
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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

    # Patch the requests.json call
    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test GithubOrgClient.public_repos to see if the list of
        repos is from the chosen payload"""

        # Set the payload result
        payload = [{"name": "Test_name"}]
        # If get_json is called, make payload the result
        mock_json.return_value = payload
        # Start a patch context with a mod for properties
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            # Set the resurn value of the patch to desired value
            mock.return_value = True
            # Create an instance
            github_client = GithubOrgClient("org_name")
            # Call the function that we want to test
            result = github_client.public_repos()
            # Retrieve the expected result
            expected = [key['name'] for key in payload]
            # Compare their values
            self.assertEqual(result, expected)

            # COnfirm that both patched methods and properties
            # were called only once
            mock.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the method GithubOrgClient.has_license"""

        test_client = GithubOrgClient("test_org")
        result = test_client.has_license(repo, license_key)

        self.assertEqual(result, expected)


@parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class for an integration test to only mock code that sends external
    requests"""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up a mock get method to be used for tests in this class"""

        # This side effect turned out to be unneccesary for task 8
        #def side_effect(url):
        #    """Side effect function for the test"""

        #    # This is the url to retrieve all the data
        #    print(url)
        #    test_url = "https://api.github.com/orgs/google"
        #    # If url is valid
        #    if url == test_url:
        #        return cls.org_payload
        #    # Else returm the remaining repo data
        #    return cls.repos_payload

        config = {'return_value.json.side_effecct':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        # print(config)
        cls.get_patcher = patch('requests.get', **config)
        cls.mock_get = cls.get_patcher.start()

    # def test_public_repos(self):
    #    """Method to test the integrated call"""
    #    github_client = GithubOrgClient("org_name")
    #    self.assertEqual(github_client.public_repos(), self.expected_repos)

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down the created patcher"""
        cls.get_patcher.stop()

test = TestIntegrationGithubOrgClient()
