#!/usr/bin/env python3
"""Type annotated module"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Function to sum a list of different types"""

    return sum(mxd_list)
