import re


RED = 12
GREEN = 13
BLUE = 14


def main():
    with open("input.txt", "r") as f:
        possible_game_ids: list[int] = []
        for line in (l.rstrip("\n") for l in f.readlines()):
            game_id_match = re.search(r"^Game (\d+):", line)
            assert game_id_match
            game_id = int(game_id_match.group(1))

            sets_str_match = re.search(r": (.+)$", line)
            assert sets_str_match

            game_is_good = True
            for set_ in sets_str_match.group(1).split(";"):
                set_ = set_.strip()

                red_count_match = re.search(r"(\d+) red", set_)
                if red_count_match:
                    red_count = int(red_count_match.group(1))
                    game_is_good = game_is_good and (red_count <= RED)

                    if not game_is_good:
                        break

                green_count_match = re.search(r"(\d+) green", set_)
                if green_count_match:
                    green_count = int(green_count_match.group(1))
                    game_is_good = game_is_good and (green_count <= GREEN)

                    if not game_is_good:
                        break

                blue_count_match = re.search(r"(\d+) blue", set_)
                if blue_count_match:
                    blue_count = int(blue_count_match.group(1))
                    game_is_good = game_is_good and (blue_count <= BLUE)

                    if not game_is_good:
                        break

            if game_is_good:
                possible_game_ids.append(game_id)

    print(sum(possible_game_ids))


if __name__ == "__main__":
    main()
