"""
http://adventofcode.com/2017/day/18
"""
from typing import List

INPUT = open('input_18.txt', 'r').read()[:-1]
TEST_INPUT = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""


def operations_list(stream: str) -> List[List[str]]:
    return [x.split() for x in stream.split('\n')]


def duet(operations: str) -> int:
    operations = operations_list(operations)
    register = {}
    curr_position = 0
    last_played = None
    while 0 <= curr_position < len(operations):
        # print(operations[curr_position])
        if len(operations[curr_position]) == 3:
            operation, letter, argument = operations[curr_position]
            if argument.isalpha():
                try:
                    argument = register[argument][-1]
                except ValueError:
                    argument = 0
            else:
                argument = int(argument)
        else:
            operation, letter = operations[curr_position]
        if letter.isalpha() and letter not in register:
            register[letter] = [0]
        if operation == 'set':
            register[letter].append(argument)
        elif operation == 'add':
            register[letter].append(register[letter][-1] + argument)
        elif operation == 'mul':
            register[letter].append(register[letter][-1] * argument)
        elif operation == 'mod':
            register[letter].append(register[letter][-1] % argument)
        elif operation == 'rcv' and register[letter][-1] > 0:
            return last_played
        elif operation == 'snd':
            last_played = register[letter][-1]
        elif operation == 'jgz':
            if letter.isalpha():
                letter = register[letter][-1]
                if letter > 0:
                    curr_position += argument
                    continue
        curr_position += 1
    return -1

assert duet(TEST_INPUT) == 4

if __name__ == '__main__':
    print(duet(INPUT))
