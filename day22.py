"""
http://adventofcode.com/2017/day/22
"""
from typing import Tuple

import time

from day21 import to_image
import numpy as np

INPUT = open('input_22.txt', 'r').read()[:-1]
TEST_INPUT = """..#
#..
..."""


class Grid:
    def __init__(self, stream: str) -> None:
        array = to_image(stream)
        self.infected = []
        self.status = {}  # 0 - clean, 1 - weakened, 2 - infected, 3 - flagged
        size = array.shape
        center = [s//2 for s in size]
        for i, row in enumerate(array):
            for j, x in enumerate(row):
                if x == 1:
                    self.infected.append((i - center[0], j - center[1]))
                    self.status[(i - center[0]) + (j - center[1])*1j] = 2
                else:
                    self.status[(i - center[0]) + (j - center[1])*1j] = 0
        self.curr_pos = np.array([0, 0])
        self.counter_infections = 0
        self.movement = np.array([-1, 0])

    def infect(self, node: np.ndarray) -> None:
        self.infected.append(tuple(node))
        self.counter_infections += 1

    def clean(self, node: np.ndarray) -> None:
        self.infected.remove(tuple(node))

    def turn_node(self, node: np.ndarray) -> None:
        try:
            curr = self.status[node[0] + node[1] * 1j]
        except KeyError:
            self.status[node[0] + node[1] * 1j] = 0
            curr = 0
        if curr == 1:
            self.counter_infections += 1
        self.status[node[0] + node[1] * 1j] = (curr + 1) % 4

    def is_infected(self, node: np.ndarray) -> bool:
        return tuple(node) in self.infected

    def move(self):
        """
        If virus moves to right it's position changes by [0, 1], and then it has to go
        left ([-1, 0]) or right ([1, 0]). Depending on it infected status it chooses turn.
        If node was infected it cleans it and turns right, otherwise it infects it and turns left.
        initial move -> left turn, right turn
        [0, 1] -> [-1, 0], [1, 0] R
        [0, -1] -> [1, 0], [-1, 0] L
        [-1, 0] -> [0, -1], [0, 1] U
        [1, 0] -> [0, 1], [0, -1] D
        """
        if self.is_infected(self.curr_pos):
            self.clean(self.curr_pos)
            self.movement = [self.movement[1], -self.movement[0]]
        else:
            self.infect(self.curr_pos)
            self.movement = [-self.movement[1], self.movement[0]]
        self.curr_pos += self.movement

    def complicated_move(self):
        pos = self.curr_pos[0] + self.curr_pos[1] * 1j
        try:
            curr = self.status[pos]
        except KeyError:
            self.status[pos] = 0
            curr = 0
        if curr == 2:
            self.movement = [self.movement[1], -self.movement[0]]
        elif curr == 3:
            self.movement = [-self.movement[0], -self.movement[1]]
        elif curr == 0:
            self.movement = [-self.movement[1], self.movement[0]]
        self.turn_node(self.curr_pos)
        self.curr_pos += self.movement

    def activities(self, number: int) -> int:
        for _ in range(number):
            self.move()
        return self.counter_infections

    def complicated_activities(self, number: int) -> int:
        for i in range(number):
            if i % 100000 == 0:
                print(i)
            self.complicated_move()
        return self.counter_infections


g = Grid(TEST_INPUT)
# assert g.activities(7) == 5
# assert g.activities(70) == 41
# assert g.activities(10000) == 5587

assert g.complicated_activities(100) == 26
# assert g.complicated_activities(10_000_000) == 2511944

if __name__ == '__main__':
    grid = Grid(INPUT)
#     print(grid.activities(10000))
    time0 = time.time()
    print(grid.complicated_activities(10_000_000))
    print(time.time() - time0)