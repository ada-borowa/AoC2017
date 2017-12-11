"""
http://adventofcode.com/2017/day/11
Cube coordinates for hexagon grid:
https://www.redblobgames.com/grids/hexagons/#coordinates-cube
"""
from typing import List, Tuple


class HexField(object):
    x: int = 0
    y: int = 0
    z: int = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def move(self, direction: str) -> None:
        if direction == 'n':
            self.y += 1
            self.z -= 1
        elif direction == 's':
            self.y -= 1
            self.z += 1
        elif direction == 'ne':
            self.x += 1
            self.z -= 1
        elif direction == 'se':
            self.x += 1
            self.y -= 1
        elif direction == 'nw':
            self.x -= 1
            self.y +=1
        elif direction == 'sw':
            self.x -= 1
            self.z += 1
    
    def distance(self, field: 'HexField') -> int:
        return max(abs(self.x - field.x), abs(self.y - field.y), abs(self.z - field.z))

    def show(self):
        return self.x, self.y, self.z


def find_coordinate(instructions: List[str]) -> Tuple[int, int, int]:
    child = HexField(0, 0, 0)
    for instruction in instructions:
        child.move(instruction)
    return child.show()

# Test Part1

START = HexField(0, 0, 0)
point1 = HexField(*find_coordinate(['ne', 'ne', 'ne']))
point2 = HexField(*find_coordinate(['ne', 'ne', 'sw', 'sw']))
point3 = HexField(*find_coordinate(['ne', 'ne', 's', 's']))
point4 = HexField(*find_coordinate(['se', 'sw', 'se', 'sw', 'sw']))

assert START.distance(point1) == 3
assert START.distance(point2) == 0
assert START.distance(point3) == 2
assert START.distance(point4) == 3


def find_max_distance(instructions: List[str]) -> int:
    curr_max = 0
    child = HexField(0, 0, 0)
    for instruction in instructions:
        child.move(instruction)
        curr_dist = START.distance(child)
        if curr_dist > curr_max:
            curr_max = curr_dist
    return curr_max


INPUT = open('input_11.txt', 'r').read().strip().split(',')

if __name__ == '__main__':
    print(START.distance(HexField(*find_coordinate(INPUT))))
    print(find_max_distance(INPUT))
