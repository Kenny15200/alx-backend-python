#!/usr/bin/env python3
"""
Safely Get Value
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value associated with the key in the dictionary if it exists, otherwise returns the default value.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key in the dictionary, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default

