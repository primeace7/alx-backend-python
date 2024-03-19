#!/usr/bin/env python3
'''create a list of async tasks and return them'''


import asyncio
from typing import Iterable
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> Iterable[asyncio.Task]:
    result = []
    for i in range(n):
        output = await task_wait_random(max_delay)
        result.append(output)
    return result
