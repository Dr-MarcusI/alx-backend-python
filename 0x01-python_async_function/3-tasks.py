#!/usr/bin/env python3
"""do not create an async function, use the regular function """
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    max_delay and returns a asyncio.Task
    regular function syntax to do this) task_wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
