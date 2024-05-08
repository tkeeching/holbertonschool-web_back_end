#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension
    four times in parallel
    """

    start_time = asyncio.get_event_loop().time()  # Record start time

    # Execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())

    end_time = asyncio.get_event_loop().time()  # Record end time

    total_runtime = end_time - start_time
    return total_runtime


# Test
# async def main():
#     return await(measure_runtime())

# print(
#     asyncio.run(main())
# )
