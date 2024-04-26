#!/usr/bin/env python3
"""sumary_line"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    endtime = time.time()
    runtime = endtime - start_time
    return runtime
