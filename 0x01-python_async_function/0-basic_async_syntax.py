#!/usr/bin/env python3
import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    x = random.uniform(0, max_delay)

    await asyncio.sleep(x)
    return x
