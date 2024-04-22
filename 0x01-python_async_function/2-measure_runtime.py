#!/usr/bin/env python3
"""this is an async function"""


from asyncio import run
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        float: _description_
    """
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time / n
