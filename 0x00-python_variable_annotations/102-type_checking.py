#!/usr/bin/env python3

"""
Zoom Array

This module defines a function to zoom into an array by repeating its elements.

"""

from typing import Tuple, Any

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zoom into an array by repeating its elements.

    Args:
        lst (Tuple[Any, ...]): The input tuple.
        factor (int): The zoom factor. Default is 2.

    Returns:
        Tuple[Any, ...]: The zoomed-in tuple.

    """
    zoomed_in = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

