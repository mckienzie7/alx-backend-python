#!/usr/bin/env python3
"""complex mixed. List with mixed float and integer."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """sum of values of list is returned"""
    return sum(mxd_lst)
