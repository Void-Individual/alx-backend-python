#!/usr/bin/env python3
"""Module on the basics of async"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """An async coroutine that waits for a randomly generated
    number and returns the number"""

    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)

    return random_number
