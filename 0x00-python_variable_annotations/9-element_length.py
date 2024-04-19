#!/usr/bin/env python3
"""this is the comment"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element length function"""
    return [(i, len(i)) for i in lst]
