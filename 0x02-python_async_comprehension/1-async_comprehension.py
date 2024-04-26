#!/usr/bin/env python3
"""sumary_line"""


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return [i async for i in async_generator()]
