import re


def parse(file: str) -> list:
    with open(file, "r") as f:
        return f.readlines()


def iterate_through(multiply: list) -> list:
    p = r"\d+"
    results = []
    for x in multiply:
        results.append(re.findall(p, x))
    return results


def find_size(dimensions: list) -> int:
    size = 0
    for x in range(len(dimensions)):
        a, b, c = int(dimensions[x][0]), int(dimensions[x][1]), int(dimensions[x][2])
        smallest = min([a * b, b * c, c * a])
        size += (2 * a * b) + (2 * b * c) + (2 * c * a) + smallest
    return size


def find_size_ribbon(dimensions: list) -> int:
    size = 0
    for x in range(len(dimensions)):
        a, b, c = int(dimensions[x][0]), int(dimensions[x][1]), int(dimensions[x][2])
        smallest = min([a + b, b + c, c + a])
        size += (a * b * c) + (2 * smallest)
    return size


def main():
    matches = iterate_through(parse("input.txt"))
    print("surface area",find_size(matches))
    print("ribbon length",find_size_ribbon(matches))


main()
