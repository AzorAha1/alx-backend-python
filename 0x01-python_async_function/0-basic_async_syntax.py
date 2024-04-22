#!/usr/bin/env python3
"""this is async function"""

import random


async def wait_random(max_delay: int = 10) -> float:
    """function to return a random"""
    return random.uniform(0, max_delay)
