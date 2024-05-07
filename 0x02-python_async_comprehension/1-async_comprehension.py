#!/usr/bin/env python3
"""Async Comprehension"""
import asyncio
async_generator = __import__('0-async_generator').async_generator
from typing import List

async def async_comprehension() -> List[float]:
    """
    A async comprehension coroutine that give random list,
    By iterating through the async object
    """
    result = [i async for i in async_generator()]
    return result
