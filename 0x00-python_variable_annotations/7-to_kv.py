#!/usr/bin/env python3
"""Type annotated module"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function to annotate a string alonside int/float as a tuple"""

    return (k, (v * v))
