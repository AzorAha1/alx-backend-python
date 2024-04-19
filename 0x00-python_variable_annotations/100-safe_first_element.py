#!/usr/bin/env python3
"""this is the comment"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe first element"""
    if lst:
        return lst[0]
    else:
        return None
