#!/usr/bin/env python3
'''Task 0's module
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Async Function that eventually returns a random delay
    '''
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
