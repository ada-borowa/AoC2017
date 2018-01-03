"""
http://adventofcode.com/2017/day/24
"""
from typing import List, Tuple

TEST_INPUT = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""

INPUT = open('input_24.txt', 'r').read()[:-1]


def create_comp_list(stream: str) -> List[Tuple[int, int]]:
    components = []
    for row in stream.split('\n'):
        a, b = [int(x) for x in row.split('/')]
        components.append((a, b))
    return components


def starting_points(components: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return [x for x in components if x[0] == 0]


def bridge_value(bridge: List[Tuple[int, int]]) -> int:
    return sum([a+b for a, b in bridge])


def create_bridges(bridges, components: List[Tuple[int, int]], start: Tuple[int, int], curr_path=[]) -> None:
    components = components[:]
    curr_path = curr_path[:]
    components.remove(start if start in components else (start[1], start[0]))
    curr_path.append(start)
    next_points = [x for x in components if start[1] in x]
    if len(next_points) == 0:
        bridges.append(curr_path)
    else:
        for n in next_points:
            if n not in curr_path:
                n = n if start[1] == n[0] else (n[1], n[0])
                create_bridges(bridges, components, n, curr_path)
        bridges.append(curr_path)


def get_max_value(stream: str) -> int:
    comps = create_comp_list(stream)
    all_bridges = []
    for s in starting_points(comps):
        create_bridges(all_bridges, comps, s)
    return max([(bridge_value(x)) for x in all_bridges])


def get_longest_bridge(stream: str) -> int:
    comps = create_comp_list(stream)
    all_bridges = []
    for s in starting_points(comps):
        create_bridges(all_bridges, comps, s)
    longest = max([len(x) for x in all_bridges])
    return max([(bridge_value(x)) for x in all_bridges if len(x) == longest])


assert get_max_value(TEST_INPUT) == 31
assert get_longest_bridge(TEST_INPUT) == 19

if __name__ == '__main__':
    print('Part 1:', get_max_value(INPUT))
    print('Part 2:', get_longest_bridge(INPUT))