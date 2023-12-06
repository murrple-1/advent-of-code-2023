import string
from collections import defaultdict
from functools import reduce


def main():
    with open("input.txt", "r") as f:
        line_list = [l.rstrip("\n") for l in f.readlines()]

    symbols: dict[tuple[int, int, str], list[int]] = defaultdict(list)

    for i, line in enumerate(line_list):
        start_j = 0
        reading_number = False
        for j, c in enumerate(line):
            if reading_number:
                if c not in string.digits:
                    reading_number = False
                    for x, y, symbol in _adjacent_engine_symbols(
                        line_list, start_j, j, i
                    ):
                        symbols[(x, y, symbol)].append(int(line[start_j:j]))
                elif j >= (len(line) - 1):
                    for x, y, symbol in _adjacent_engine_symbols(
                        line_list, start_j, j, i
                    ):
                        symbols[(x, y, symbol)].append(int(line[start_j : j + 1]))
            else:
                if c in string.digits:
                    if j >= (len(line) - 1):
                        for x, y, symbol in _adjacent_engine_symbols(
                            line_list, start_j, j, i
                        ):
                            symbols[(x, y, symbol)].append(int(line[j]))
                    else:
                        start_j = j
                        reading_number = True

    print(
        sum(
            reduce(lambda a, b: a * b, l)
            for ((_, _, symbol), l) in symbols.items()
            if symbol == "*" and len(l) == 2
        )
    )


def _adjacent_engine_symbols(
    line_list: list[str], start_j: int, end_j: int, i: int
) -> list[tuple[int, int, str]]:
    adjacent_engine_symbols: list[tuple[int, int, str]] = []
    for i_ in range(max(i - 1, 0), min(i + 2, len(line_list)), 1):
        for j_ in range(max(start_j - 1, 0), min(end_j + 1, len(line_list[i])), 1):
            if i_ == i and start_j < j_ < end_j:
                continue

            if (c := line_list[i_][j_]) not in string.digits and c != ".":
                adjacent_engine_symbols.append((i_, j_, c))

    return adjacent_engine_symbols


if __name__ == "__main__":
    main()
