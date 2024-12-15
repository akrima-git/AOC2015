import re

p1 = r"a|e|i|o|u"
p2 = r"(.)\1"
p3 = r"ab|cd|pq|xy"

p12 = r"(.{2}).*\1"
p22 = r"(.)\w\1"

def parse(file):
    with open(file, "r") as f:
        return f.readlines()


def naughty_or_nice(string_input: list):
    total = 0
    for x in string_input:
        x = x.strip()
        one = re.findall(p1, x)
        two = re.findall(p2, x)
        three = re.findall(p3, x)
        print(one, two, three)
        if len(one) >= 3 and len(two) >= 1 and len(three) == 0:
            total += 1
            print("good")
    return total

def naughty_or_nice2(string_input: list):
    total = 0
    for x in string_input:
        x = x.strip()
        one = re.findall(p12, x)
        two = re.findall(p22, x)
        print(one, two)
        if len(one) >= 1 and len(two) >= 1:
            total += 1
            print("good")
    return total

def main():
    print(naughty_or_nice(parse("input.txt")))
    print(naughty_or_nice2(parse("input.txt")))


main()
