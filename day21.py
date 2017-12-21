"""
http://adventofcode.com/2017/day/21
"""
from typing import List, Tuple
import numpy as np

START = """.#.
..#
###"""

TEST_RULES = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""

RULES = open('input_21.txt', 'r').read()[:-1]


def to_image(stream: str) -> np.ndarray:
    arr = [[x for x in row] for row in stream.split('\n')]
    return np.array([[1 if x == '#' else 0 for x in row] for row in arr])


def rule_to_img(stream: str) -> Tuple[np.ndarray, np.ndarray]:
    r1, r2 = stream.replace('/', '\n').split(' => ')
    return to_image(r1), to_image(r2)


def rotate(pixel: np.ndarray) -> np.ndarray:
    return np.rot90(pixel)


def flip_horizontal(pixel: np.ndarray) -> np.ndarray:
    return np.flip(pixel, axis=0)


def flip_vertical(pixel: np.ndarray) -> np.ndarray:
    return np.flip(pixel, axis=1)


def match(pixel: np.ndarray, rule: np.ndarray) -> bool:
    for _ in range(4):
        if np.array_equal(pixel, rule):
            return True
        if np.array_equal(flip_horizontal(pixel), rule):
            return True
        if np.array_equal(flip_vertical(pixel), rule):
            return True
        pixel = rotate(pixel)
    return False


def enhance(pixel: np.ndarray,
            rules_2: List[Tuple[np.ndarray, np.ndarray]],
            rules_3: List[Tuple[np.ndarray, np.ndarray]],
            iterations: int) -> np.ndarray:
    for c in range(iterations):
        print(c)
        size = pixel.shape[0]
        if size % 2 == 0:
            new_pixel = np.zeros((size//2*3, size//2*3))
            new_i, new_j = 0, 0
            for i in range(0, size, 2):
                for j in range(0, size, 2):
                    for r2 in rules_2:
                        if match(pixel[i:i+2, j:j+2], r2[0]):
                            new_pixel[new_i:new_i + 3, new_j:new_j + 3] = r2[1]
                    new_j += 3
                    new_j %= new_pixel.shape[0]
                new_i += 3
        elif size % 3 == 0:
            new_pixel = np.zeros((size//3*4, size//3*4))
            new_i, new_j = 0, 0
            for i in range(0, size, 3):
                for j in range(0, size, 3):
                    for r3 in rules_3:
                        if match(pixel[i:i+3, j:j+3], r3[0]):
                            new_pixel[new_i:new_i + 4, new_j:new_j + 4] = r3[1]
                    new_j += 4
                    new_j %= new_pixel.shape[0]
                new_i += 4
        pixel = new_pixel
    return pixel


def count(rules_stream: str, iterations: int) -> int:
    all_rules = [rule_to_img(line) for line in rules_stream.split('\n')]
    rules_2, rules_3 = [], []
    for rule in all_rules:
        if rule[0].shape[0] == 2:
            rules_2.append(rule)
        elif rule[0].shape[0] == 3:
            rules_3.append(rule)
    pixel = to_image(START)
    enhanced_pixel = enhance(pixel, rules_2, rules_3, iterations)
    return int(sum(sum(enhanced_pixel)))

assert count(TEST_RULES, 2) == 12

if __name__ == '__main__':
    print('Part 1:', count(RULES, 5))
    print('Part 2:', count(RULES, 18))  # not th most efficient way, but works
