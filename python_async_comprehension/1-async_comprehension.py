#!/usr/bin/env python3

"""
Async generator
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension overy async_generator
    """

    random_numbers = [number async for number in async_generator()]
    return random_numbers


# Tests
# async def main():
#     print(await async_comprehension())

# asyncio.run(main())
