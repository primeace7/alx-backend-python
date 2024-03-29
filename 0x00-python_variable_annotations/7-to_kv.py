#!/usr/bin/env python3
'''
Implementation of a custom function that squares
an element of a tuple
'''


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Return the input args as a tuple with the second arg
    squared
    '''
    return (k, v**2)
