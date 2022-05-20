from flask import Flask
import Utils

app = Flask(__name__)


@app.route("/")
def Score():
    try:
        f = open(Utils.SCORES_FILE_NAME)
    except Exception:
        error = "Unable to read score file"
        massage = f"<html><head><title>Scores Game</title></head><body><body><h1><div id='score' style='color:red'>{error}</div></h1></body></html>"
        return massage
    score = f.readlines()[0]
    f.close()
    massage = f"<html><head><title>Scores Game</title></head><body><h1>The score is <div id='score'>{score}</div></h1></body></html>"
    return massage, 200  # status code


app.run(host='127.0.0.1', debug=True, port=5000)
