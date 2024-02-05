import random


user_nums = [49, 22, 35, 7, 5, 9]


def get_random_6_nums() -> list:
    return [random.randint(1, 49) for i in range(6)]


def game():
    guessing = True

    while guessing:
        curent_nums_random = get_random_6_nums()

        while True:
            try:
                user_input = list(
                    map(int, input("Pleas enter 6 nums like this:'1 2 20 30  enter': ").split(" ")))
                if len(user_input) > 6:
                    print("You give me too many numbers i need only 6")
                    raise ValueError
                elif len(user_input) < 6:
                    print("Not enought numbers i need 6")
                    raise ValueError
                break
            except ValueError as e:
                print("something went wrong:\n", e)

        break


if __name__ == "__main__":
    game()
