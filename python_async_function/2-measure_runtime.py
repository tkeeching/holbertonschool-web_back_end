#!/usr/bin/env python3

"""
Measure the runtime
"""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Returns the average execution time"""

    start_time = time.time()

    await wait_n(n, max_delay)

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n


# Tests
# n = 5
# max_delay = 9

# print(asyncio.run(measure_time(n, max_delay)))
