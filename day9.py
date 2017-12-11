"""
http://adventofcode.com/2017/day/9
{} - contains group
<> - contains trash
! - cancels next character
"""

# each { will be stored as 1 in a list acting as the stack
# score of group is depth of GROUP stack when the group is closed
GROUP = []


def count_group_score(stream: str) -> int:
    stream = [x for x in stream]
    score = 0
    in_garbage = False
    while stream:
        character = stream.pop(0)
        if character == '!':
            stream.pop(0)
        elif character == '<' and not in_garbage:
            in_garbage = True
        elif character == '>' and in_garbage:
            in_garbage = False
        elif character == '{' and not in_garbage:
            GROUP.append(1)
        elif character == '}' and not in_garbage:
            score += len(GROUP)
            GROUP.pop()
    return score


def count_garbage(stream: str) -> int:
    stream = [x for x in stream]
    garbage_count = 0
    in_garbage = False
    while stream:
        character = stream.pop(0)
        if character == '!':
            stream.pop(0)
        elif character == '<' and not in_garbage:
            in_garbage = True
        elif character == '>' and in_garbage:
            in_garbage = False
        elif character == '{' and not in_garbage:
            GROUP.append(1)
        elif character == '}' and not in_garbage:
            GROUP.pop()
        elif in_garbage:
            garbage_count += 1

    return garbage_count

# Test part 1

assert count_group_score('{}') == 1
assert count_group_score('{{{}}}') == 6.
assert count_group_score('{{},{}}') == 5.
assert count_group_score('{{{},{},{{}}}}') == 16.
assert count_group_score('{<a>,<a>,<a>,<a>}') == 1.
assert count_group_score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
assert count_group_score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
assert count_group_score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3

# Test part 2

assert count_garbage('<>') == 0
assert count_garbage('<random characters>') == 17
assert count_garbage('<<<<>') == 3
assert count_garbage('<{!>}>') == 2
assert count_garbage('<!!>') == 0
assert count_garbage('<!!!>>') == 0
assert count_garbage('<{o"i!a,<{i<a>') == 10

if __name__ == '__main__':
    stream = open('input_9.txt', 'r').read()
    print(count_group_score(stream))
    print(count_garbage(stream))



