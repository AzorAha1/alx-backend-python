#!/usr/bin/env python3
"""this is an async function"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_
    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        list[float]: _description_
    """
    listofdelays = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*listofdelays)
    return results
