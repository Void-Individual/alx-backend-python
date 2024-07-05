#!/usr/bin/env python3
"""Type annotated module"""

from typing import Sequence, Any, Union, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Function to increase the size of an array by a factor"""

    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
