#!/usr/bin/env python3
'''Execute multiple coroutines with async'''


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay:int) -> List[float]:
    '''
    spawn an async coroutine n times and gather
    the return values
    '''
    output = []
    for i in range(n):
        result = await wait_random(max_delay)
        output.append(result)
    return sorted(output)
