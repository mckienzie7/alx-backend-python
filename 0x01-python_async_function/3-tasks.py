#!/usr/bin/env python3

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from asyncio import Task

def task_wait_random(max_delay: int) -> Task[float]:
    return asyncio.create_task(wait_random(max_delay))

