#!/usr/bin/env python3
'''asyncly retrieve 10 random numbers from an async generator'''


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''retrieve and return a list of asyncly generated numbers'''
    result = []
    async for i in async_generator():
        result.append(i)
    return result
