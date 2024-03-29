#!/usr/bin/env python3
'''
Implement an annotated multiplier function that takes a
function as an arg
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Implement a multiplier-maker function
    '''
    def multiply(const: float) -> float:
        '''return a float multiplier'''
        return multiplier * const

    return multiply
