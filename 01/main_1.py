import re


def main():
    with open("input.txt", "r") as f:
        sum_ = 0
        for line in (l.rstrip("\n") for l in f.readlines()):
            first_match = re.search(r"^[^\d]*(\d)", line)
            last_match = re.search(r"(\d)[^\d]*$", line)
            assert first_match
            assert last_match
            sum_ += int(first_match.group(1) + last_match.group(1))

        print(sum_)


if __name__ == "__main__":
    main()
