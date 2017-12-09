"""
http://adventofcode.com/2017/day/4
"""
from typing import List


def check_line1(line: str) -> bool:
    words = line.strip('\n').split(' ')
    for i, m in enumerate(words):
        for j, n in enumerate(words):
            if i == j:
                continue
            if m == n:
                return False
    return True


def validate_1(lines: List[str]) -> int:
    output = 0
    for line in lines:
        if check_line1(line):
            output += 1
    return output


def check_line2(line):
    words = line.strip('\n').split(' ')
    for i, m in enumerate(words):
        for j, n in enumerate(words):
            if i == j:
                continue
            if sorted(m) == sorted(n):
                return False
    return True


def validate_2(lines: List[str]) -> int:
    output = 0
    for line in lines:
        if check_line2(line):
            output += 1
    return output


INPUT_4 = open('input_4.txt', 'r').readlines()

if __name__ == '__main__':

    # Part 1

    assert validate_1(['aa bb cc dd ee',
                       'aa bb cc dd aa',
                       'aa bb cc dd aaa']) == 2

    print(validate_1(INPUT_4))

    # Part 2

    assert validate_2(['abcde fghij',
                       'abcde xyz ecdab',
                       'a ab abc abd abf abj',
                       'iiii oiii ooii oooi oooo',
                       'oiii ioii iioi iiio']) == 3

    print(validate_2(INPUT_4))