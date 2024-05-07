#!/usr/bin/env python3

"""
Multiple coroutines with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays"""

    result = []

    while n > 0:
        result.append(await wait_random(max_delay))
        n -= 1

    return sorted(result)


# Tests
# print(asyncio.run(wait_n(5, 5)))
# print(asyncio.run(wait_n(10, 7)))
# print(asyncio.run(wait_n(10, 0)))
