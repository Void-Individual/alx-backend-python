#!/usr/bin/env python3
"""Type annotated module"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function to return the sum of a list of floats"""

    sum: float = 0
    for x in input_list:
        sum += x

    return sum
