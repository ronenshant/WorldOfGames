import random
import time

from WorldOfGames.MemoryGame import clearConsole


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty*3)
    return secret_number


def get_guss_from_user(difficulty):
    # noinspection PyBroadException
    try:
        guess = int(input(f"Please guess a number from 1 to {difficulty*3}:"))
    except Exception:
        print("No.. pleas enter number \n")
        guess = 0
        get_guss_from_user(difficulty)
    return guess


def compare_results(secret, guess):
    if secret == guess:
        return True
    else:
        return False


def play(difficulty):
    game_on = True
    secret_num = generate_number(difficulty)
    while game_on:
        if compare_results(secret_num, get_guss_from_user(difficulty)):
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
                    to_continue = input("Not what we expected!! Please type [y/n]")
    return print("Sorry, But You Lost the game\n")
