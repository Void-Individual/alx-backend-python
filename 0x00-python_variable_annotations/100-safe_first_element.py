#!/usr/bin/env python3
"""Type annotated module"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function to retireve the first element of an iterable, else
    return nothing"""

    if lst:
        return lst[0]
    else:
        return None
