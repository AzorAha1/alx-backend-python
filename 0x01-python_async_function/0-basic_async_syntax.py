#!/usr/bin/env python3
import random


"""this is async function"""


async def wait_random(max_delay=10):
    """function to return a random"""
    return random.uniform(0, max_delay)
