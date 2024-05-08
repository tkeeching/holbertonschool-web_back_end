#!/usr/bin/env python3

"""
Multiple coroutines with async
"""
import asyncio
from asyncio.tasks import Task
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays"""

    result = []

    while n > 0:
        result.append(await task_wait_random(max_delay))
        n -= 1

    return sorted(result)


# Tests
# n = 5
# max_delay = 6
# print(asyncio.run(task_wait_n(n, max_delay)))

