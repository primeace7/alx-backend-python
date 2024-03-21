#!/usr/bin/env python3
'''Implement an async generator'''


import time
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, int]:
    '''asyncrhronously gnerate random floats'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
