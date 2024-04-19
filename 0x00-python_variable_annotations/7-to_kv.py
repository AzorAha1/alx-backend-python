#!/usr/bin/env python3
"""function with type annotation"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to k v"""
    return (k, v ** 2)
