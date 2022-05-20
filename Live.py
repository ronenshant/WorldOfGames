from GuessGame import play
from MemoryGame import memory_play
from CurrencyRouletteGame import currency_play
from Score import *


def welcome(name):
    return "Hello " + name + " and welcome to the wold of games (WoG).\nHere you can find many cool games to play\n"


def load_game():
    game = 0
    difficulty = 0
    is_game_good = False
    is_diff_good = False
    continue_to_play = True
    while not is_game_good:
        # noinspection PyBroadException
        try:
            game = int(input("Please choose a game to play:\n"
                             "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess "
                             "it back\n"
                             "2. Guess Game - guess a number and see if you chose like the computer\n"
                             "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                             "4. Exit\n"))
        except Exception:
            print("No.. input is not a number.\n")
        if type(game) != int:
            print("Please Enter Number\n")
        elif game == 4:
            return
        elif game in range(1, 4):
            is_game_good = True
        else:
            print("Enter game number 1 to 3 or 4 to exit\n")

    while not is_diff_good:
        # noinspection PyBroadException
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5:\n"))
        except Exception:
            print("No.. input is not a number.\n")
        if difficulty in range(1, 6):
            is_diff_good = True
        else:
            continue
    while continue_to_play:
        if game == 1:
            if memory_play(difficulty) == 1:
                add_score(difficulty)
            game = 0
            load_game()
        elif game == 2:
            if play(difficulty) == 1:
                add_score(difficulty)
            game = 0
            load_game()
        elif game == 3:
            if currency_play(difficulty) == 1:
                add_score(difficulty)
            game = 0
            load_game()
        else:
            continue_to_play = False
    return
