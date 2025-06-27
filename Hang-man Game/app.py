from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

with open("words.txt", "r") as file:
    WORDS = file.read().strip().split(",")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new-word")
def new_word():
    word = random.choice(WORDS).upper()
    return jsonify({"word": word})

if __name__ == "__main__":
    app.run(debug=True)
