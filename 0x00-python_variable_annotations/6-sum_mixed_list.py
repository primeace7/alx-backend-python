#!/usr/bin/env python3
'''Implementation of a list-summing function'''


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Return the sum of a list of floats as a float'''
    return float(sum(mxd_lst))
