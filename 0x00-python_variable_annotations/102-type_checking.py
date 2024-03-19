#!/usr/bin/env python3
'''Fixing custom function's annotation '''


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''return an input list duplicated by a factor'''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
