"""
http://adventofcode.com/2017/day/25
"""
from typing import Dict, Tuple

TEST_INPUT = """Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A."""

INPUT = open('input_25.txt', 'r').read()[:-1]


def parse_input(stream: str) -> Tuple[str, int, Dict]:
    lines = stream.split('\n')
    start_state = lines[0].split()[-1].strip('.')
    number_of_steps = [int(s) for s in lines[1].split() if s.isdigit()][0]
    rules = {}
    i = 3
    while i < len(lines):
        curr_lines = lines[i: i + 9]
        curr_state = curr_lines[0].split()[-1].strip(':')
        value_if_0 = int(curr_lines[2].split()[-1].strip('.'))
        move_if_0 = curr_lines[3].split()[-1].strip('.')
        state_if_0 = curr_lines[4].split()[-1].strip('.')
        value_if_1 = int(curr_lines[6].split()[-1].strip('.'))
        move_if_1 = curr_lines[7].split()[-1].strip('.')
        state_if_1 = curr_lines[8].split()[-1].strip('.')
        rules[curr_state] = [[value_if_0, move_if_0, state_if_0],
                             [value_if_1, move_if_1, state_if_1]]
        i += 10
    return start_state, number_of_steps, rules


def turing_machine(stream: str) -> int:
    curr_state, number_of_steps, rules = parse_input(stream)
    curr_place = 0
    curr_value = 0
    tape = {curr_place: curr_value}
    for _ in range(number_of_steps):
        curr_value, next_move, curr_state = rules[curr_state][curr_value]
        tape[curr_place] = curr_value
        curr_place = curr_place + 1 if next_move == 'right' else curr_place - 1
        curr_value = 0 if curr_place not in tape else tape[curr_place]
    return sum([tape[x] for x in tape.keys()])

assert turing_machine(TEST_INPUT) == 3

if __name__ == '__main__':
    print(turing_machine(INPUT))

