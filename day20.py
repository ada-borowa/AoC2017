"""
http://adventofcode.com/2017/day/20
"""
from typing import List

import numpy as np

TEST_INPUT = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"""


class Particle:
    def __init__(self, line):
        p, v, a = line.split(', ')
        self.p = np.array([int(x) for x in p.lstrip('p=<').rstrip('>').split(',')])
        self.v = np.array([int(x) for x in v.lstrip('v=<').rstrip('>').split(',')])
        self.a = np.array([int(x) for x in a.lstrip('a=<').rstrip('>').split(',')])

    def move(self):
        self.v += self.a
        self.p += self.v

    def print_particle(self):
        print(self.p)

    def distance_to_0(self):
        return sum([abs(x) for x in self.p])

    def abs_acceleration(self):
        return sum([abs(x) for x in self.a])


def solve_collisions(particles: List[Particle]) -> None:
    positions = np.array([p.p for p in particles])
    sums = (positions[:, np.newaxis] == positions).all(axis=2).sum(axis=1)
    for i in range(len(sums) - 1, -1, -1):
        if sums[i] > 1:
            particles.remove(particles[i])


INPUT = open('input_20.txt', 'r').read()

if __name__ == '__main__':
    particles = [Particle(line) for line in INPUT.split('\n')[:-1]]
    print('Part 1:', np.argmin([p.abs_acceleration() for p in particles]))
    for _ in range(100):
        for p in particles:
            p.move()
        if len(np.unique([p.p for p in particles], axis=0)) < len(particles):
            solve_collisions(particles)
    print('Part 2:', len(particles))

