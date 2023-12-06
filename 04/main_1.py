def main():
    with open("input.txt", "r") as f:
        points_list: list[int] = []

        for line in (l.rstrip("\n") for l in f.readlines()):
            _, num_part = line.split(":", 1)

            winning_num_part, has_num_part = num_part.split("|", 1)

            winning_nums = frozenset(
                int(n) for n in winning_num_part.strip().split(" ") if n != ""
            )
            has_nums = frozenset(
                int(n) for n in has_num_part.strip().split(" ") if n != ""
            )

            wins = len(winning_nums.intersection(has_nums))
            points = 2 ** (wins - 1) if wins > 0 else 0
            points_list.append(points)

    print(sum(points_list))


if __name__ == "__main__":
    main()
