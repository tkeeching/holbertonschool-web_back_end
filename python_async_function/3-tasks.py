#!/usr/bin/env python3

"""
Tasks
"""
import asyncio
from asyncio.tasks import Task
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Returns a asyncio.Task"""

    return asyncio.create_task(wait_random(max_delay))


# Tests
# async def test(max_delay: int) -> float:
#     task = task_wait_random(max_delay)
#     await task
#     print(task.__class__)

# asyncio.run(test(5))
