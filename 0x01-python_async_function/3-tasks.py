#!/usr/bin/python3
'''Create and return an async task from a sync function'''


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''return an async task from a sync fucntion'''
    return asyncio.create_task(wait_random(max_delay))
