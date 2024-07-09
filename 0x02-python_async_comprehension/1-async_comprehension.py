#!/usr/bin/env python3
"""Module containing an async printing coroutine"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine to collect 10 random numbers from a generator and then
    return the numbers"""

    random_numbers = []
    async for i in async_generator():
        random_numbers.append(i)

    return random_numbers
