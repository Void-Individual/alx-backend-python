#!/usr/bin/env python3
"""Type annotated module"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that takes a float and returns a function that
    multiplies a float with the value, to return a float"""

    def multiplier_function(value: float) -> float:

        return multiplier * value

    return multiplier_function
