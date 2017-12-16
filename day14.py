"""
http://adventofcode.com/2017/day/14
"""
from typing import List, Tuple

import numpy as np

from day10_2 import knot_hash

INPUT = 'hfdlxzhv'
SIZE = (128, 128)
NUMBERS = [a for a in range(256)]


def hash_input(key: str, row: int) -> str:
    return key + '-' + str(row)

assert hash_input(INPUT, 5) == 'hfdlxzhv-5'


def hex2bin(hash: str):
    binary = ''
    for h in hash:
        binary += '{0:04b}'.format(int(h, 16))
    return binary


def defragmentation(key: str) -> np.ndarray:
    disk = []
    for i in range(0, SIZE[0]):
        hex_hash = knot_hash(hash_input(key, i), NUMBERS.copy())
        bin_hash = hex2bin(hex_hash)
        disk.append([int(x) for x in bin_hash])
    disk = np.array(disk)
    return disk


def count_squares(disk: List[List[int]]) -> int:
    return sum(sum(disk))

TEST_INPUT = 'flqrgnkx'

assert count_squares(defragmentation(TEST_INPUT)) == 8108


def adjacent_cells(cell: Tuple[int, int]) -> List[Tuple[int, int]]:
    i, j = cell
    cells = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for c in cells:
        if c[0] < 0 or c[0] > SIZE[0] - 1 or c[1] < 0 or c[1] > SIZE[1] - 1:
            cells.remove(c)
    return cells


def check_group(start: Tuple[int, int], number: int, disk: np.ndarray) -> None:
    queue = [start]
    disk[start[0], start[1]] = number
    while queue:
        q = queue.pop()
        cells = adjacent_cells(q)
        for c in cells:
            if disk[c] == -1:
                disk[c] = number
                queue.append(c)


def find_new_group(disk: np.ndarray) -> Tuple[int, int]:
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            if disk[i, j] == -1:
                return i, j
    return -1, -1


def count_groups(disk: np.ndarray) -> int:
    disk *= -1
    curr_number = 0
    while True:
        new_group = find_new_group(disk)
        if new_group == (-1, -1):
            return curr_number - 1
        check_group(new_group, curr_number, disk)
        curr_number += 1

assert count_groups(defragmentation(TEST_INPUT)) == 1242

if __name__ == '__main__':
    print(count_squares(defragmentation(INPUT)))
    print(count_groups(defragmentation(INPUT)))