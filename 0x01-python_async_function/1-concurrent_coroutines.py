#!/usr/bin/env python3
import asyncio
from typing import List


wait_random_f = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, wait_random: int) -> List[float]:
    asc = []
    for i in range(n):
        x = await wait_random_f(wait_random)
        ind = 0
        while ind < len(asc) and asc[ind] < x:
            ind += 1
        asc.insert(ind, x)

    return asc
