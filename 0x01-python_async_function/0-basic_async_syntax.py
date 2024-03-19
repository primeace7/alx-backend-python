#!/usr/bin/env python3
'''Implementation of a basic asynchronous coroutine'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''generage and return a random float asynchronously'''
    result = random.uniform(0, max_delay)
    await asyncio.sleep(result)
    return result
