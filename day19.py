"""
http://adventofcode.com/2017/day/19
"""
from typing import Tuple

TEST_INPUT = """     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+ """
MOVES = [[1, 0], [-1, 0], [0, 1], [0, -1]]


class Map:
    def __init__(self, stream: str):
        self.map = [[x for x in row] for row in stream.split('\n')]
        self.movement = [1, 0]  # down, [-1, 0] - up, [0, 1] - right, [0, -1] -left
        self.path = ''
        self.x, self.y = self.find_start()
        self.steps = 0

    def print_map(self):
        print('\n'.join([''.join(row) for row in self.map]))

    def find_start(self) -> Tuple[int, int]:
        for i, row in enumerate(self.map):
            for j, x in enumerate(row):
                if x == '|':
                    return i, j

    def check_next(self):
        try:
            a = self.map[self.x][self.y]
            if a == ' ':
                return False
        except IndexError:
            return False
        return True

    def move(self):
        field = self.map[self.x][self.y]
        if field == '+':
            options = [[a, b] for [a, b] in MOVES if [a, b] != [-m for m in self.movement]]
            for op in options:
                try:
                    if self.map[self.x + op[0]][self.y + op[1]] != ' ':
                        self.movement = op
                except IndexError:
                    continue
        else:
            if field.isalpha():
                self.path += field
        self.x += self.movement[0]
        self.y += self.movement[1]
        return self.check_next()

    def travel(self):
        while True:
            a = self.move()
            self.steps += 1
            if not a:
                return self.path

TEST_MAP = Map(TEST_INPUT)
assert TEST_MAP.travel() == 'ABCDEF'
assert TEST_MAP.steps == 38

INPUT = open('input_19.txt', 'r').read()[:-1]

if __name__ == '__main__':
    map1 = Map(INPUT)
    print(map1.travel())
    print(map1.steps)



