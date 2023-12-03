import re

_number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main():
    with open("input.txt", "r") as f:
        sum_ = 0
        number_regex_str = "|".join(_number_map.keys())
        reverse_number_regex_str = "|".join(k[::-1] for k in _number_map.keys())

        regex_str = rf"^.*?({number_regex_str}|\d)"
        reverse_regex_str = rf"^.*?({reverse_number_regex_str}|\d)"

        for line in (l.rstrip("\n") for l in f.readlines()):
            first_match = re.search(regex_str, line)
            last_match = re.search(reverse_regex_str, line[::-1])
            assert first_match
            assert last_match

            sum_ += int(
                f"{_convert_to_int_str(first_match.group(1))}{_convert_to_int_str(last_match.group(1)[::-1])}"
            )

        print(sum_)


def _convert_to_int_str(s: str) -> str:
    return _number_map.get(s, s)


if __name__ == "__main__":
    main()
