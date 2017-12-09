"""
http://adventofcode.com/2017/day/2
"""
from typing import List


def str_2_row(line: str) -> List[int]:
    """Makes list of numbers out of string with numbers separated by tab."""
    row = line.strip('\n').split()
    row = [int(r) for r in row]
    return row


def checksum_1(lines: List[str]) -> int:
    """For each line finds minimum and maximum, answer is sum of differences."""
    output = 0
    for line in lines:
        row = str_2_row(line)
        output += max(row) - min(row)
    return output


def checksum_2(lines: List[str]) -> int:
    """For each line finds 2 numbers: one divides other evenly, then sums results of division."""
    output = 0
    for line in lines:
        row = str_2_row(line)
        n1, n2 = 0, 0
        for j in row:
            for k in row:
                if not j == k:
                    if k % j == 0 or j % k == 0:
                        n1, n2 = j, k
        output += max([n1, n2])//min([n1, n2])
    return output


INPUT_2 = open('input_2.txt', 'r').readlines()
INPUT_TEST1 = ['5 1 9 5',
               '7 5 3',
               '2 4 6 8']
INPUT_TEST2 = ['5 9 2 8',
               '9 4 7 3',
               '3 8 6 5']

if __name__ == '__main__':

    # Part 1

    assert checksum_1(INPUT_TEST1) == 18

    print(checksum_1(INPUT_2))

    # Part 2


    assert checksum_2(INPUT_TEST2) == 9

    print(checksum_2(INPUT_2))
