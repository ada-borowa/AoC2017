"""
http://adventofcode.com/2017/day/23
"""


class Register:
    def __init__(self) -> None:
        self.register = {}
        self.counter_mul = 0
        self.curr_pos = 0

    def value(self, r: str) -> int:
        if not r.isalpha():
            return int(r)
        else:
            try:
                return self.register[r]
            except KeyError:
                self.register[r] = 0
                return 0

    def operation(self, line: str) -> None:
        op, x, y = line.split()
        if x.isalpha() and x not in self.register:
            self.register[x] = 0
        if op == 'set':
            self.register[x] = self.value(y)
        elif op == 'sub':
            self.register[x] -= self.value(y)
        elif op == 'mul':
            self.register[x] *= self.value(y)
            self.counter_mul += 1
        elif op == 'jnz':
            if self.value(x) != 0:
                self.curr_pos += self.value(y)
            else:
                self.curr_pos += 1
        if op != 'jnz':
            self.curr_pos += 1

    def run_program(self, instructions: str) -> int:
        instructions = instructions.split('\n')
        while 0 <= self.curr_pos < len(instructions):
            line = instructions[self.curr_pos]
            self.operation(line)
        return self.counter_mul


def composite(number: int):
    i = 2
    while i**2 <= number:
        if number % i == 0:
            return True
        i += 1
    return False


INPUT = open('input_23.txt', 'r').read()[:-1]

if __name__ == '__main__':
    r = Register()
    print('Part 1:', r.run_program(INPUT))
    print('Part 2:')
    b = 93 * 100 + 100_000
    c = b + 17000
    h = 0
    while True:
        if composite(b):
            h += 1
        if b == c:
            break
        b += 17
    print(h)

