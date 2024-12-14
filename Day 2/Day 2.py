import re

p = r"\d+"


def parse(file: str) -> list:
    with open(file, "r") as f:
        return f.readlines()


def iterate_through(multiply: list) -> list:
    results = []
    for x in multiply:
        results.append(re.findall(p, x))
    return results


def find_size(dimensions: list) -> int:
    size = 0
    for x in range(len(dimensions)):
        a = int(dimensions[x][0])
        b = int(dimensions[x][1])
        c = int(dimensions[x][2])
        smallest = min([a * b, b * c, c * a])
        size += (2 * a * b) + (2 * b * c) + (2 * c * a) + smallest
    return size


def main():
    matches = iterate_through(parse("input.txt"))
    print(find_size(matches))


main()


def find_size_ribbon(dimensions: list) -> int:
    size = 0
    for x in range(len(dimensions)):
        a = int(dimensions[x][0])
        b = int(dimensions[x][1])
        c = int(dimensions[x][2])
        smallest = min([a + b, b + c, c + a])
        size += (a * b * c) + (2 * smallest)
    return size

def main_two():
    matches = iterate_through(parse("input.txt"))
    print(find_size_ribbon(matches))

main_two()
