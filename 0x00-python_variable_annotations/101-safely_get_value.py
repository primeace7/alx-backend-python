#!/usr/bin/env python3
'''Duck typing a custom function with unknown types and return values'''


from typing import TypeVar, Mapping, Hashable, Union, Any
T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    '''return a dictinary entry or a default value'''
    if key in dct:
        return dct[key]
    else:
        return default
