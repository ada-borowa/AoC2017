"""
http://adventofcode.com/2017/day/10
Part 1 (part 2 is in the second file)
"""
from typing import List


def twisty_hash(numbers: List[int], instructions: List[int]) -> List[int]:
    position = 0
    skip = 0
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


assert twisty_hash([a for a in range(5)], [3, 4, 1, 5]) == [3, 4, 2, 1, 0]

if __name__ == '__main__':
    numbers = [a for a in range(256)]
    instructions = [int(a) for a in open('input_10.txt', 'r').read().split(',')]
    twisted_list = twisty_hash(numbers, instructions)
    print(twisted_list[0] * twisted_list[1])
