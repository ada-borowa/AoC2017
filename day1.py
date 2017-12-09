"""
http://adventofcode.com/2017/day/1
"""


def captcha_1(number: str) -> int:
    """Adds number if the next number is the same."""
    output = 0
    for i, x in enumerate(number):
        if int(x) == int(number[(i + 1) % len(number)]):
            output += int(x)
    return output


def captcha_2(number: str) -> int:
    """Adds number if the number halfway through the list is the same."""
    output = 0
    for i, x in enumerate(number[:len(number)//2]):
        if int(x) == int(number[(i + len(number)//2)]):
            output += int(x) * 2
    return output

# Input file's name is 'input_1.txt')
INPUT_1 = open('input_1.txt', 'r').readlines()[0].strip('\n')

if __name__ == '__main__':

    # Part 1

    assert captcha_1('1122') == 3
    assert captcha_1('1111') == 4
    assert captcha_1('1234') == 0
    assert captcha_1('91212129') == 9

    print(captcha_1(INPUT_1))

    # Part 2

    assert captcha_2('1212') == 6
    assert captcha_2('1221') == 0
    assert captcha_2('123425') == 4
    assert captcha_2('123123') == 12
    assert captcha_2('12131415') == 4

    print(captcha_2(INPUT_1))


