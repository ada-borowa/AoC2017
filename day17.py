"""
http://adventofcode.com/2017/day/17
"""
from typing import List, Tuple

import time

INPUT = 343
REPS2 = 50_000_000


def spin_lock(step: int, reps: int) -> Tuple[List[int], int]:
    buffer = [0]
    curr_value = 0
    position = 0
    for i in range(reps):
        position = (position + step) % len(buffer)
        curr_value += 1
        position += 1
        buffer.insert(position, curr_value)
    return buffer, position


assert spin_lock(3, 1) == ([0, 1], 1)
assert spin_lock(3, 2) == ([0, 2, 1], 1)
assert spin_lock(3, 3) == ([0, 2, 3, 1], 2)


def value_after_last(buffer: List[int], position: int) -> int:
    return buffer[(position + 1) % len(buffer)]

assert value_after_last(*spin_lock(3, 2017)) == 638


def spin_lock_no_buffer(step: int, reps: int) -> int:
    curr_len = 1
    curr_pos = 0
    curr_value = 0
    after_0 = 0
    time0 = time.time()
    for i in range(reps):
        curr_pos = (curr_pos + step) % curr_len + 1
        curr_value += 1
        if curr_pos == 1:
            after_0 = curr_value
        curr_len += 1
    print('Time:', time.time() - time0)
    return after_0

assert spin_lock_no_buffer(3, 4) == 2
assert spin_lock_no_buffer(3, 6) == 5
assert spin_lock_no_buffer(3, 9) == 9


if __name__ == '__main__':
    print(value_after_last(*spin_lock(INPUT, 2017)))
    print(spin_lock_no_buffer(INPUT, REPS2))