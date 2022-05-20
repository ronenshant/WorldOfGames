import os

global SCORES_FILE_NAME
SCORES_FILE_NAME = "Scores.txt"
global BAD_RETURN_CODE
BAD_RETURN_CODE = 666


def UtilsClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
    print("\n"*100)

