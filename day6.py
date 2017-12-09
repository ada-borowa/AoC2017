"""
http://adventofcode.com/2017/day/6
"""
import numpy as np


def distribute(banks):
    lst = banks
    idx = np.argmax(lst)
    amount = lst[idx]
    lst[idx] = 0
    curr_id = (idx + 1) % len(lst)
    while amount > 0:
        lst[curr_id] += 1
        curr_id = (curr_id + 1) % len(lst)
        amount -= 1
    return lst

banks = open('input_6.txt', 'r').readlines()
banks = [int(x) for x in banks[0].strip('\n').split('\t')]
previous = [banks[:]]
count = 0
while True:
    count += 1
    banks = distribute(banks)
    if banks in previous:
        print('Part 1:', count)
        print('Part 2:', count - previous.index(banks))
        break
    previous.append(banks[:])
