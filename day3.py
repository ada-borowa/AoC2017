"""
http://adventofcode.com/2017/day/3
"""
import math

import numpy as np


def get_position(number: int) -> int:
    """Gets position of number when numbers are arranged in spiral with 1 in position [0,0]."""
    if number == 1:
        return 0
    position = [0, 1]
    step = 1
    multiplier = 2
    base = 1
    while step < number - 1:
        if step < base + multiplier - 1:
            position[0] -= 1
        elif step < base + 2 * multiplier - 1:
            position[1] -= 1
        elif step < base + 3 * multiplier - 1:
            position[0] += 1
        elif step < base + 4 * multiplier - 1:
            position[1] += 1
        else:
            base = step + 1
            multiplier += 2
            position[1] += 1
        step += 1
    return int(math.fabs(position[0]) + math.fabs(position[1]))


def bigger_number(number: int) -> int:
    """Finds the first value bigger than 'number' in table where cells are sum of all adjacent sells.
    Put into static table for simplicity."""
    inputs = np.zeros([1000, 1000])
    inputs[500, 500] = 1
    position = [500, 501]
    step = 1
    multiplier = 2
    base = 1
    while step < number:
        inputs[position[0], position[1]] = sum(
            sum(inputs[position[0] - 1:position[0] + 2, position[1] - 1:position[1] + 2]))
        if inputs[position[0], position[1]] > number:
            return int(inputs[position[0], position[1]])
        if step < base + multiplier - 1:
            position[0] -= 1
        elif step < base + 2 * multiplier - 1:
            position[1] -= 1
        elif step < base + 3 * multiplier - 1:
            position[0] += 1
        elif step < base + 4 * multiplier - 1:
            position[1] += 1
        else:
            base = step + 1
            multiplier += 2
            position[1] += 1
        step += 1

if __name__ == '__main__':

    assert get_position(1) == 0
    assert get_position(12) == 3
    assert get_position(23) == 2
    assert get_position(1024) == 31

    print(get_position(265149))

    print(bigger_number(265149))
