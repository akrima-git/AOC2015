x = ""


def parse(file):
    global x
    x = [x for x in open("input.txt")]


def one():
    parse("input.txt")
    print(list(x[0]).count("(") - list(x[0]).count(")"))


def two():
    floor = 0
    parse("input.txt")
    for i, char in enumerate(x[0]):
        floor += 1 if char == "(" else -1
        if floor == -1:
            print(i)
            return


one()
two()
