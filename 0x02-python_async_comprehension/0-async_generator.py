#!/usr/bin/env python3
"""sumary_line"""


import asyncio
import random


async def async_generator():
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        therandom = random.uniform(0, 10)
        yield therandom
