import random
import os
import time


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
    print("\n"*100)


def generate_sequence(difficulty):
    rand_list = [random.randrange(1, 101, 1) for i in range(difficulty)]
    return rand_list


def get_list_from_user(difficulty):
    guess = []
    temp = 0
    for i in range(difficulty):
        # noinspection PyBroadException
        try:
            temp = int(input(f"please enter number in place {i + 1} : "))
        except Exception:
            print("No.. pleas enter number \n")
            guess = []
            # get_list_from_user(difficulty)
            return
        guess.append(int(temp))
    print(f" Your guess is {guess} ...\n")
    return guess


def is_list_equal(list1, list2):
    if list1 == list2:
        return True
    else:
        return False


def memory_play(difficulty):
    game_on = True
    rand_list = generate_sequence(difficulty)
    print(rand_list)
    time.sleep(difficulty)
    clearConsole()
    while game_on:
        user_list = get_list_from_user(difficulty)
        equal = is_list_equal(rand_list, user_list)
        if equal:
            print("\nVery Good, you wan the game\n")
            time.sleep(3)
            clearConsole()
            return
        else:
            to_continue = input("Nop!! \nDo you want to try again?[y/n]\n")
            try_again = True
            while try_again:
                if to_continue.lower() == "y":
                    try_again = False
                elif to_continue.lower() == "n":
                    game_on = False
                    try_again = False
                else:
                    to_continue = input("Not what we expected!! Please type [y/n]\n")
    print("Sorry, But You Lost the game\n")
    return
