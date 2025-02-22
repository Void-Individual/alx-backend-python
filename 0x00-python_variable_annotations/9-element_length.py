#!/usr/bin/env python3
"""Type annotated module"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function to return the length of the iterables in a passed list"""

    return [(i, len(i)) for i in lst]
