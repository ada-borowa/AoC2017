"""
http://adventofcode.com/2017/day/5
"""
from typing import List


def operations1(ops: List[int]) -> int:
    curr_id = 0
    counter = 0
    while curr_id < len(ops):
        curr_jump = ops[curr_id]
        ops[curr_id] += 1
        curr_id += curr_jump
        counter += 1
    return counter


def operations2(ops: List[int]) -> int:
    curr_id = 0
    counter = 0
    while curr_id < len(ops):
        curr_jump = ops[curr_id]
        if curr_jump >= 3:
            ops[curr_id] -= 1
        else:
            ops[curr_id] += 1
        curr_id += curr_jump
        counter += 1
    return counter


INPUT_5 = [int(x.strip('\n')) for x in open('input_5.txt', 'r').readlines()]

if __name__ == '__main__':

    # Part 1

    # copy to reuse list
    INPUT_5_copy = INPUT_5[:]

    assert operations1([0, 3, 0, 1, -3]) == 5

    print(operations1(INPUT_5))

    # Part 2

    assert operations2([0, 3, 0, 1, -3]) == 10

    print(operations2(INPUT_5_copy))
