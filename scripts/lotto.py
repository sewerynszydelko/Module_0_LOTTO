import random

ONE_GAME_PRICE = 3
WEEKS_IN_YEAR = 52

def get_random_6_nums() -> set:
    return set(random.randint(1, 49) for i in range(6))


def get_user_num() -> set:
    while True:
        try:
            user_input = list(
                map(int, input("Pleas enter 6 nums like this:'1 2 20 30  enter': ").split(" ")))
            if len(set(user_input)) > 6:
                print("You give me too many numbers i need only 6")
                raise ValueError
            elif len(set(user_input)) < 6:
                print("Not enought numbers i need 6\nand only orginal no duplicate!")
                raise ValueError
            break
        except ValueError as e:
            print("something went wrong:\n", e)
    return set(user_input)

def cost_and_years_to_win(count_trys) -> str:

    cost_game = count_trys * ONE_GAME_PRICE
    how_many_years_to_win = count_trys // WEEKS_IN_YEAR

    final_info = f"If we asume you will play once in week you need a {how_many_years_to_win:,} years and it will cost you {cost_game:,} zł if 1 game = 3 zł"

    return final_info

def game():
    count_trys = 0
    user_choice = get_user_num()

    while True:
        count_trys += 1
        curent_nums_random = get_random_6_nums()

        if user_choice == curent_nums_random:
            print(f"congratulation it took's {count_trys} trys\n")
            break

        if count_trys == 10000000:
            print(f"It's took already {count_trys} trys\n")
            break
    
    final_info = cost_and_years_to_win(count_trys)

    return print(final_info)


if __name__ == "__main__":
    game()
