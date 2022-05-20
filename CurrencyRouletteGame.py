import time
import random
from currency_converter import CurrencyConverter
from WorldOfGames.MemoryGame import clearConsole


def get_money_interval(difficulty):
    c = CurrencyConverter()
    currency = c.convert(1, 'USD', 'ILS')
    t = random.randrange(1, 100, 1)
    guess_range = [(t - (5 - difficulty)) * float(currency), (t + (5 - difficulty)) * float(currency)]
    return guess_range, t


def get_guess_from_user(total):
    # noinspection PyBroadException
    try:
        guess = float(input(f"How mach NIS is {total} USD?"))
    except Exception:
        print("No.. pleas enter number \n")
        guess = 0
        get_guess_from_user(total)
    return guess


def currency_play(difficulty):
    game_on = True
    result = get_money_interval(difficulty)
    guess_range = result[0]
    total = result[1]

    while game_on:
        guess = get_guess_from_user(total)
        if guess_range[0] <= guess <= guess_range[1]:
            print("\nVery Good, you wan the game\n")
            time.sleep(2)
            clearConsole()
            return
        else:
            try_again = True
            to_continue = input("Nop!! \nDo you want to try again?[y/n]\n")
            while try_again:
                if to_continue.lower() == "y":
                    try_again = False
                elif to_continue.lower() == "n":
                    game_on = False
                    try_again = False
                else:
                    to_continue = input("Not what we expected!! Please type [y/n]")
    return print("Sorry, But You Lost the game\n")
