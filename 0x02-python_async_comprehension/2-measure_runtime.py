#!/usr/bin/env python3
'''measure the runtime of a group of tasks running asyncly'''


import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''asyncly execute a group of async functions and measure
    their runtime
    '''
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.time() - start_time
