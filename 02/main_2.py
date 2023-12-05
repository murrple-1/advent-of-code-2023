import re
from dataclasses import dataclass


@dataclass
class Counts:
    red: int
    green: int
    blue: int


def main():
    with open("input.txt", "r") as f:
        min_counts: list[Counts] = []
        for line in (l.rstrip("\n") for l in f.readlines()):
            sets_str_match = re.search(r": (.+)$", line)
            assert sets_str_match

            min_count = Counts(0, 0, 0)
            for set_ in sets_str_match.group(1).split(";"):
                set_ = set_.strip()

                red_count_match = re.search(r"(\d+) red", set_)
                if red_count_match:
                    red_count = int(red_count_match.group(1))
                    min_count.red = max(min_count.red, red_count)

                green_count_match = re.search(r"(\d+) green", set_)
                if green_count_match:
                    green_count = int(green_count_match.group(1))
                    min_count.green = max(min_count.green, green_count)

                blue_count_match = re.search(r"(\d+) blue", set_)
                if blue_count_match:
                    blue_count = int(blue_count_match.group(1))
                    min_count.blue = max(min_count.blue, blue_count)

            min_counts.append(min_count)

    print(sum((mc.red * mc.green * mc.blue) for mc in min_counts))


if __name__ == "__main__":
    main()
