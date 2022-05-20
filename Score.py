import os.path

import Utils


def add_score(dif):
    file_exists = os.path.exists(Utils.SCORES_FILE_NAME)
    if file_exists:
        f = open(Utils.SCORES_FILE_NAME)
        last_score = f.readlines()[0]
        f.close()
        print(last_score)
    else:
        last_score = "0"
        f = open(Utils.SCORES_FILE_NAME, 'w')
        f.write(last_score)
        f.close()
    new_score = (dif * 3) + 5
    total_score = new_score + int(last_score)
    f = open(Utils.SCORES_FILE_NAME, 'w')
    f.write(str(total_score))
    f.close()



