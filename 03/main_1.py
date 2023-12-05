import string


def main():
    with open("input.txt", "r") as f:
        line_list = [l.rstrip("\n") for l in f.readlines()]

    engine_numbers: list[int] = []

    for i, line in enumerate(line_list):
        start_j = 0
        reading_number = False
        for j, c in enumerate(line):
            if reading_number:
                if c not in string.digits:
                    reading_number = False
                    if _is_engine_num(line_list, start_j, j, i):
                        engine_numbers.append(int(line[start_j:j]))
                elif j >= (len(line) - 1):
                    if _is_engine_num(line_list, start_j, j, i):
                        engine_numbers.append(int(line[start_j : j + 1]))
            else:
                if c in string.digits:
                    if j >= (len(line) - 1):
                        if _is_engine_num(line_list, start_j, j, i):
                            engine_numbers.append(int(line[j]))
                    else:
                        start_j = j
                        reading_number = True

    print(sum(engine_numbers))
    # print("\n".join(str(i) for i in engine_numbers))


def _is_engine_num(line_list: list[str], start_j: int, end_j: int, i: int) -> bool:
    for i_ in range(max(i - 1, 0), min(i + 3, len(line_list)), 1):
        for j_ in range(max(start_j - 1, 0), min(end_j + 2, len(line_list[i])), 1):
            if i_ == i and start_j < j_ < end_j:
                continue

            if (c := line_list[i_][j_]) not in string.digits and c != ".":
                return True
    return False
    # return True


if __name__ == "__main__":
    main()
