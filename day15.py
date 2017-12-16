"""
http://adventofcode.com/2017/day/15
"""

START_A = 634
START_B = 301
FACTOR_A = 16807
FACTOR_B = 48271
DIVIDER = 2147483647
PAIRS = 40 * 10**6
PAIRS2 = 5 * 10**6


def check(a: int, b: int) -> bool:
    return bin(a)[-16:] == bin(b)[-16:]


def judge(a: int, b: int, pairs: int) -> int:
    curr_A = a
    curr_B = b
    count = 0
    for i in range(pairs):
        if i % 1000 == 0:
            print(i)
        curr_A = (curr_A * FACTOR_A) % DIVIDER
        curr_B = (curr_B * FACTOR_B) % DIVIDER
        if check(curr_A, curr_B):
            count += 1
    return count


def judge2(a: int, b: int, pairs: int) -> int:
    curr_A = a
    curr_B = b
    count = 0
    to_judge = 0
    numbers_A = []
    numbers_B = []
    while to_judge < pairs:
        curr_A = (curr_A * FACTOR_A) % DIVIDER
        curr_B = (curr_B * FACTOR_B) % DIVIDER
        if curr_A % 4 == 0:
            numbers_A.append(curr_A)
            if len(numbers_A) <= len(numbers_B):
                to_judge += 1
                if check(numbers_A[-1], numbers_B[len(numbers_A) - 1]):
                    count += 1
        if curr_B % 8 == 0:
            numbers_B.append(curr_B)
            if len(numbers_B) <= len(numbers_A):
                to_judge += 1
                if check(numbers_A[len(numbers_B) - 1], numbers_B[-1]):
                    count += 1
    return count

TEST_A = 65
TEST_B = 8921
TEST_PAIRS = 5
TEST_PAIRS2 = 1056

assert judge(TEST_A, TEST_B, TEST_PAIRS) == 1
assert judge2(TEST_A, TEST_B, TEST_PAIRS2) == 1

if __name__ == '__main__':
    print(judge(START_A, START_B, PAIRS))
    print(judge2(START_A, START_B, PAIRS2))
