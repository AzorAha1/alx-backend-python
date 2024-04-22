#!/usr/bin/env python3
"""this is an async function"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        list[float]: _description_
    """
    listofdelays = []
    for _ in range(n):
        listofdelays.append(wait_random(max_delay))
    results = await asyncio.gather(*listofdelays)
    return results
