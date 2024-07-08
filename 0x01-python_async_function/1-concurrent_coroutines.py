#!/usr/bin/env python3
"""Module on the basics of async"""

import asyncio
from typing import List
import heapq

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function to run the wait_random co-routine a specified
    number of times"""

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    heapq.heapify(delays)
    return [heapq.heappop(delays) for _ in range(len(delays))]
