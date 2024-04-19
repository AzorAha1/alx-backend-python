#!/usr/bin/env python3
"""this is the comment"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier function"""
    def multiplier_function(x: float) -> float:
        """multiplier function"""
        return multiplier * x
    return multiplier_function
