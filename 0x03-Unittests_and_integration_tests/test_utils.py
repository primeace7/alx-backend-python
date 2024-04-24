#!/usr/bin/env python3
'''Test utils.access_nested_map function'''
from parameterized import parameterized
import requests
from utils import (
    access_nested_map,
    get_json,
    memoize
    )
import unittest
from unittest.mock import (
    patch,
    Mock,
    PropertyMock
    )
from typing import (
    Mapping,
    Sequence,
    Any
    )


class TestAccessNestedMap(unittest.TestCase):
    '''Test case for access_nested_map function'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: Any) -> None:
        '''Test function return value'''
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        '''Test that exception is raised for invalid input'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Test case for get_json function'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        '''Test that get_json returns the right data'''
        mock = Mock()
        mock.json = Mock(return_value=test_payload)
        with patch('requests.get', return_value=mock) as mocker:
            self.assertEqual(get_json(test_url), test_payload)
            mocker.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''Test case for the memoize decorator'''

    def test_memoize(self):
        '''Test the @memoize decorator'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            example = TestClass()
            self.assertEqual(example.a_property, 42)
            self.assertEqual(example.a_property, 42)
            mock.assert_called_once()
