import re

p = r"on|off|toggle"
p2 = r"\d+"

x = ["off" for x in range(1000 * 1000)]


def parse(file: str) -> list:
    orders = [line.strip() for line in open(file)]
    return orders


def on_or_off(list_input):
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
                    x[index] = "off" if x[index] == "on" else "on"
                    continue
                x[index] = switch

    print(x.count("on"))


on_or_off(parse("input.txt"))
