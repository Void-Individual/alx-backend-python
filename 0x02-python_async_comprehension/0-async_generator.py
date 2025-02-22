#!/usr/bin/env python3
"""Module containing an async generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """A coroutine to run in 10 loops, waiting 1 second after each
    one and yielding a random number each time"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
