#!/usr/bin/env python3
"""10 random numbers using an async comprehensing over"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension - function that takes no arguments
    Return: 10 random numbers
    """
    rslt = [i async for i in async_generator()]
    return rslt
