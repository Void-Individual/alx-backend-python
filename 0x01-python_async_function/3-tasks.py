#!/usr/bin/env python3
"""Module on the basics of async"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function to run a random number and return its async format"""

    return asyncio.create_task(wait_random(max_delay))
