#!/usr/bin/env python3

"""
Asynchronous coroutine that takes in an interger argument ('max_delay',
with a default value of 10) named 'wait_random' that waits for a random
delay between 0 and 'max_delay' (included and float value) seconds and
eventually returns it
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns random delay in seconds"""

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


# Tests
# print(asyncio.run(wait_random()))
# print(asyncio.run(wait_random(5)))
# print(asyncio.run(wait_random(15)))
