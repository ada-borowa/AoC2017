"""
http://adventofcode.com/2017/day/12
"""
from typing import Dict, List


def neighbour_lists(stream: str) -> Dict[int, List[int]]:
    lines = stream.split('\n')
    neighbours = {}
    for line in lines:
        try:
            main_program, neighbour_program = line.split(' <-> ')
            neighbour_program = [int(n) for n in neighbour_program.split(',')]
        except ValueError:
            pass
        if int(main_program) in neighbours.keys():
            neighbours[int(main_program)] += neighbour_program
        else:
            neighbours[int(main_program)] = neighbour_program
    return neighbours


TEST_INPUT1 = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

assert neighbour_lists(TEST_INPUT1) == {0: [2], 1: [1], 2: [0, 3, 4], 3: [2, 4], 4: [2, 3, 6], 5: [6], 6: [4, 5]}


def depth_first_search(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited

assert len(depth_first_search(neighbour_lists(TEST_INPUT1), 0)) == 6


def find_how_many_gropus(graph: Dict[int, List[int]]) -> int:
    accounted_for = []
    count = 0
    for i in range(max(graph.keys()) + 1):
        if i in graph.keys() and i not in accounted_for:
            visited = depth_first_search(graph, i)
            for v in visited:
                accounted_for.append(v)
            count += 1
    return count

assert find_how_many_gropus(neighbour_lists(TEST_INPUT1)) == 2

INPUT = open('input_12.txt', 'r').read()

if __name__ == '__main__':
    graph = neighbour_lists(INPUT)
    print('Part 1:', len(depth_first_search(graph, 0)))
    print('Part 2:', find_how_many_gropus(graph))