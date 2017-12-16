"""
http://adventofcode.com/2017/day/16
"""
from typing import List

PROGRAMS = [chr(i) for i in range(97, 97+16)]
TEST_PROGRAMS = PROGRAMS[:5]
TEST_INSTRUCTIONS = ['s1', 'x3/4', 'pe/b']
REPETITIONS = 1*10**9


def spin(programs: List[str], number: int) -> List[str]:
    programs = programs[-number:] + programs[:-number]
    return programs

assert spin(TEST_PROGRAMS.copy(), 3) == ['c', 'd', 'e', 'a', 'b']


def exchange(programs: List[str], pos1: int, pos2: int) -> List[str]:
    programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
    return programs

assert exchange(TEST_PROGRAMS.copy(), 3, 4) == ['a', 'b', 'c', 'e', 'd']


def partner(programs: List[str], letter1: str, letter2: str) -> List[str]:
    id1 = [i for i in range(len(programs)) if programs[i] == letter1][0]
    id2 = [i for i in range(len(programs)) if programs[i] == letter2][0]
    programs[id1], programs[id2] = letter2, letter1
    return programs

assert partner(TEST_PROGRAMS.copy(), 'e', 'b') == ['a', 'e', 'c', 'd', 'b']


def dance(programs: List[str], instructions: List[str]) -> List[str]:
    for instruction in instructions:
        if instruction[0] == 's':
            number = instruction[1:]
            programs = spin(programs, int(number))
        elif instruction[0] == 'x':
            pos1, pos2 = instruction[1:].split('/')
            programs = exchange(programs, int(pos1), int(pos2))
        elif instruction[0] == 'p':
            letter1, letter2 = instruction[1:].split('/')
            programs = partner(programs, letter1, letter2)
    return programs

assert ''.join(dance(TEST_PROGRAMS.copy(), TEST_INSTRUCTIONS)) == 'baedc'


def find_cycle(programs: List[str], instructions: List[str]) -> int:
    initial = programs[:]
    for i in range(REPETITIONS):
        programs = dance(programs, instructions)
        if programs == initial:
            return i + 1


def billion_dance(programs: List[str], instructions: List[str]) -> List[str]:
    cycle = find_cycle(programs.copy(), instructions)
    for i in range(REPETITIONS % cycle):
        programs = dance(programs, instructions)
    return programs

INPUT = open('input_16.txt', 'r').read()

assert ''.join(billion_dance(TEST_PROGRAMS.copy(), TEST_INSTRUCTIONS)) == 'abcde'

if __name__ == '__main__':
    print(''.join(dance(PROGRAMS, INPUT.split(','))))
    print(''.join(billion_dance(PROGRAMS.copy(), INPUT.split(','))))


