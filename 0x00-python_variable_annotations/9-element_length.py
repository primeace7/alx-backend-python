#!/usr/bin/python3
'''Duck typing an iterable object'''


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return a list of tuples given an iterable'''
    return [(i, len(i)) for i in lst]
