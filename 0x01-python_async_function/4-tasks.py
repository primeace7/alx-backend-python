#!/usr/bin/python3
'''create a list of async tasks and return them'''


import asyncio
task_wait_random = __import__('3-tasks').task_wait_random
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[asyncio.Task]:
    result = []
    for i in range(n):
        output = await task_wait_random(max_delay)
        result.append(output)
    return result
