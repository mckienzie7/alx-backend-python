#!/usr/bin/env python3
"""mixed list."""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of lists values as float"""
    return float(sum(mxd_lst))
