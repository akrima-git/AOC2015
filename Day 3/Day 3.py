directions_dict = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def parse(file: str) -> list:
    with open(file, "r") as f:
        return f.readlines()


def directions(houses: list) -> int:
    sum = 0
    for x in houses:
        houses_visited = set()
        start = [0, 0]
        houses_visited.add(tuple(start))
        x = x.strip()
        for y in x:
            dx, dy = directions_dict[y]
            start[0] += dx
            start[1] += dy
            houses_visited.add(tuple(start))
        sum += len(houses_visited)
    return sum


def directions_with_robot(houses: list) -> int:
    houses_visited = set()
    sum = 0
    for x in houses:
        start1, start2 = [0, 0], [0, 0]
        houses_visited.add(tuple(start1))
        x = x.strip()
        for i, y in enumerate(x):
            if i % 2 != 0:
                dx, dy = directions_dict[y]
                start1[0] += dx
                start1[1] += dy
                houses_visited.add(tuple(start1))
            else:
                dx, dy = directions_dict[y]
                start2[0] += dx
                start2[1] += dy
                houses_visited.add(tuple(start2))
        sum += len(houses_visited)
    return sum


def main():
    print("first year houses visited:", directions(parse("input.txt")))
    print("second year houses visited:", directions_with_robot(parse("input.txt")))


main()
