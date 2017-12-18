"""
http://adventofcode.com/2017/day/18
"""
import random
from typing import Any
from day18 import operations_list

INPUT = open('input_18.txt', 'r').read()[:-1]

TEST_INPUT = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""

OPERATIONS = operations_list(INPUT)


class Register:
    def __init__(self, r_id):
        self.id = r_id
        self.queue = []
        self.register = {}
        self.deadlock = False
        self.curr_pos = 0
        self.send_counter = 0

    def receive(self, value: int):
        self.queue.append(value)
        self.deadlock = False

    def recover(self, name: str):
        if name not in self.register:
            self.register[name] = self.id
        try:
            self.register[name] = self.queue.pop(0)
        except IndexError:
            self.deadlock = True

    def send(self, x: Any):
        self.send_counter += 1
        if x.isalpha():
            return self.register[x]
        else:
            return x

    def work(self, other_register: 'Register'):
        if len(OPERATIONS[self.curr_pos]) == 3:
            operation, letter, argument = OPERATIONS[self.curr_pos]
            if argument.isalpha():
                try:
                    argument = self.register[argument]
                except ValueError:
                    argument = 0
            else:
                argument = int(argument)
        else:
            operation, letter = OPERATIONS[self.curr_pos]
        if letter.isalpha() and letter not in self.register:
            self.register[letter] = self.id
        if operation == 'set':
            self.register[letter] = argument
        elif operation == 'add':
            self.register[letter] += argument
        elif operation == 'mul':
            self.register[letter] *= argument
        elif operation == 'mod':
            self.register[letter] %= argument
        elif operation == 'rcv':
            self.recover(letter)
        elif operation == 'snd':
            other_register.receive(self.send(letter))
        elif operation == 'jgz':
            if letter.isalpha():
                letter = self.register[letter]
            if int(letter) > 0:
                self.curr_pos += argument
            else:
                self.curr_pos += 1
        if operation != 'jgz' and not self.deadlock:
            self.curr_pos += 1


def duet() -> int:
    register_0 = Register(0)
    register_1 = Register(1)
    while not (register_0.deadlock and register_1.deadlock):
        if random.random() < 0.2 and not register_0.deadlock:
            register_0.work(register_1)
        if random.random() < 0.2 and not register_1.deadlock:
            register_1.work(register_0)

    return register_1.send_counter


if __name__ == '__main__':
    results = []
    print(duet())