#!/usr/bin/env python3

"""
Async generator
"""

import asyncio
import random


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)


# Tests
# async def print_yielded_values():
#     result = []
#     async for i in async_generator():
#         result.append(i)
#     print(result)

# asyncio.run(print_yielded_values())
