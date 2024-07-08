#!/usr/bin/env python3
"""Module on the basics of async"""

import asyncio
import heapq
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Co-routine to measure the average time taken for the
    previous coroutine to run"""

    start = time.monotonic()  # To record start time
    asyncio.run(wait_n(n, max_delay))
    end = time.monotonic()  # To record the end ime

    return (end - start) / n
