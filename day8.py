"""
http://adventofcode.com/2017/day/8
"""
lines = open('input_8.txt', 'r').readlines()

highest = -1000
registers = {}
for line in lines:
    register, instr, value, _, var, cond, cond_value = line.strip('\n').split(' ')
    if register not in registers:
        registers[register] = 0
    if var not in registers:
        registers[var] = 0
    if (cond == '>' and registers[var] > int(cond_value)) or\
       (cond == '<' and registers[var] < int(cond_value)) or \
       (cond == '>=' and registers[var] >= int(cond_value)) or \
       (cond == '<=' and registers[var] <= int(cond_value)) or \
       (cond == '==' and registers[var] == int(cond_value)) or \
       (cond == '!=' and registers[var] != int(cond_value)):
        if instr == 'dec':
            registers[register] -= int(value)
        elif instr == 'inc':
            registers[register] += int(value)
    if highest < max([v for v in registers.values()]):
        highest = max([v for v in registers.values()])


print('Part 1:', max([v for v in registers.values()]))
print('Part 2:', highest)

