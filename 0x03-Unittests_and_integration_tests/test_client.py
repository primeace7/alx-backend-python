#!/usr/bin/env python3
'''
Tests for client module functions
'''
import unittest
import requests
from client import GithubOrgClient
from unittest.mock import (
    patch,
    Mock,
    PropertyMock
    )
from parameterized import (
    parameterized,
    parameterized_class
    )
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''Test case for GithubOrgClient class'''
    @parameterized.expand([
        'google',
        'abc'
        ])
    @patch('client.get_json')
    def test_org(self, mock, company):
        '''Test GithubOrgClient.org method'''
        company.return_value = {'this': 'data'}
        example = GithubOrgClient(company)
        example.org
        company.assert_called_once_with(
            f'https://api.github.com/orgs/{company}')

    def test_public_repos_url(self):
        '''Test GithubOrgClient._public_repos_url method'''
        mock = PropertyMock(return_value={'repos_url': 'example.com'})
        url = 'client.GithubOrgClient.org'
        with patch(url, mock):
            example = GithubOrgClient('company')
            self.assertEqual(example._public_repos_url, 'example.com')

    @patch('client.get_json')
    def test_public_repos(self, mock):
        '''Test GithubOrgClient.public_repos method'''
        mock.return_value = [
            {'name': 'open_source_1'},
            {'name': 'open_source_2'}
            ]
        url = 'client.GithubOrgClient._public_repos_url'
        with patch(url, PropertyMock(return_value='example.com')) as mockery:
            dummy = GithubOrgClient('company')
            self.assertEqual(dummy.public_repos(),
                             ['open_source_1', 'open_source_2'])
            mock.assert_called_once()
            mockery.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, result):
        '''Test GithubOrgClient.has_license method'''
        example = GithubOrgClient('company')
        self.assertEqual(example.has_license(repo, license_key), result)


@parameterized_class([
    {'org_payload': TEST_PAYLOAD[0][0],
     'repos_payload': TEST_PAYLOAD[0][1],
     'expected_repos': TEST_PAYLOAD[0][2],
     'apache2_repos': TEST_PAYLOAD[0][3]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration test using prepared fixtures'''
    def setUpClass(self):
        mock = Mock(return_value=TEST_PAYLOAD)
        requests.get = mock
        get_patcher = patch
