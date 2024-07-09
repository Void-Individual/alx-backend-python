#!/usr/bin/env python3
"""Module to run parallel async operations"""

import asyncio
import time
async_generator = __import__('0-async_generator').async_generator


async def run_task(task):
    """Coroutine to completely consume the yield values of
    an async generator"""

    async for _ in task:
        pass


async def measure_runtime():
    """Coroutine to run 4 async operations in parallel, measure
    the runtime and return it"""

    tasks = [async_generator() for _ in range(4)]
    start = time.monotonic()
    await asyncio.gather(*[run_task(task) for task in tasks])
    end = time.monotonic()

    return (end - start)
