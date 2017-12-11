"""
http://adventofcode.com/2017/day/10
Part 2
"""
from typing import List


def instructions_to_ascii(stream: str) -> List[int]:
    """Turns stream of characters to stream of ints corresponding to their ascii codes."""
    code = []
    for s in stream:
        code.append(ord(s))
    code.extend([17, 31, 73, 47, 23])  # add constant
    return code

assert instructions_to_ascii('1,2,3') == [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]


def sparse_hash(numbers: List[int], instructions: List[int]) -> List[int]:
    position = 0
    skip = 0
    for step in range(64):
        for length in instructions:
            if length > len(numbers):
                continue
            sublist = []
            for i in range(length):
                sublist.append(numbers[(position + i) % len(numbers)])
            for i in range(length):
                numbers[(position + i) % len(numbers)] = sublist.pop()
            position = (position + length + skip) % len(numbers)
            skip += 1
    return numbers


def dense_hash(numbers: List[int]):
    hash = ''
    for i in range(16):
        xor = numbers.pop(0)
        for j in range(15):
            xor ^= numbers.pop(0)
        hash += str(hex(xor)[2:]).zfill(2)
    return hash


def knot_hash(stream: str, numbers: List[int]) -> str:
    instructions = instructions_to_ascii(stream)
    sparse = sparse_hash(numbers, instructions)
    dense = dense_hash(sparse)
    return dense

NUMBERS = [a for a in range(256)]
assert knot_hash('', NUMBERS.copy()) == 'a2582a3a0e66e6e86e3812dcb672a272'
assert knot_hash('AoC 2017', NUMBERS.copy()) == '33efeb34ea91902bb2f59c9920caa6cd'
assert knot_hash('1,2,3', NUMBERS.copy()) == '3efbe78a8d82f29979031a4aa0b16a9d'
assert knot_hash('1,2,4', NUMBERS.copy()) == '63960835bcdc130f0b66d7ff4f6a5a8e'

if __name__ == '__main__':
    instructions = open('input_10.txt', 'r').read().strip()
    print(knot_hash(instructions, NUMBERS.copy()))