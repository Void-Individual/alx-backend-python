#!/usr/bin/env python3
"""Type annotated module"""

from typing import TypeVar, Mapping, Any, Optional, Union

# Define a type variable
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """Function to return a key value if it exists in a dict, else
    return None or a fixed value"""

    if key in dct:
        return dct[key]
    else:
        return default
