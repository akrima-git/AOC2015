import re

p = r"on|off|toggle"
p2 = r"\d+"
dict_switch = {"on": 1, "off": 0}


def parse(file: str) -> list:
    return [line.strip() for line in open(file)]


def on_or_off(list_input):
    x = [0 for x in range(1000 * 1000)]
    for line in list_input:
        switch = re.search(p, line)
        switch = switch.group()
        x1, y1, x2, y2 = map(int, re.findall(p2, line))
        x2 += 1
        y2 += 1
        for i in range(x1, x2):
            for j in range(y1, y2):
                index = j * 1000 + i
                if switch == "toggle":
                    x[index] = 1 if x[index] == 0 else 0
                    continue
                x[index] = dict_switch[switch]

    print(sum(x))


def brightness(list_input):
    x = [0 for x in range(1000 * 1000)]
    for line in list_input:
        switch = re.search(p, line)
        switch = switch.group()
        x1, y1, x2, y2 = map(int, re.findall(p2, line))
        x2 += 1
        y2 += 1
        for i in range(x1, x2):
            for j in range(y1, y2):
                index = j * 1000 + i
                if switch == "toggle":
                    x[index] += 2
                elif switch == "on":
                    x[index] += 1
                elif switch == "off":
                    x[index] -= 1 if x[index] > 0 else 0
                    continue
    print(sum(x))


on_or_off(parse("input.txt"))
brightness(parse("input.txt"))
