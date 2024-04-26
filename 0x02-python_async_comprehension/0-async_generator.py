#!/usr/bin/env python3
"""sumary_line"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_descriptin
    """
    for _ in range(1, 11):
        await asyncio.sleep(1)
        therandom = random.uniform(0, 10)
        yield therandom
