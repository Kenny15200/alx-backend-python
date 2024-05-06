#!/usr/bin/env python3
"""
Make Multiplier
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float argument
        and returns the result of multiplying it by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a float by the given multiplier.

        Args:
            x (float): The float value to multiply.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return multiplier_function

