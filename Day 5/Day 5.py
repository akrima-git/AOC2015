import re


def parse(file):
    with open(file, "r") as f:
        return f.readlines()


def naughty_or_nice(string_input: list):
    p1 = r"a|e|i|o|u"
    p2 = r"(.)\1"
    p3 = r"ab|cd|pq|xy"
    total = 0
    for x in string_input:
        x = x.strip()
        one = re.findall(p1, x)
        two = re.findall(p2, x)
        three = re.findall(p3, x)
        if len(one) >= 3 and len(two) >= 1 and len(three) == 0:
            total += 1
    return total


def naughty_or_nice2(string_input: list):
    p1 = r"(.{2})\w*\1"
    p2 = r"(.)\w\1"

    total = 0
    for x in string_input:
        x = x.strip()
        one = re.findall(p1, x)
        two = re.findall(p2, x)
        if len(one) >= 1 and len(two) >= 1:
            total += 1
    return total


def main():
    print("part 1:", naughty_or_nice(parse("input.txt")))
    print("part 2:", naughty_or_nice2(parse("input.txt")))


main()
