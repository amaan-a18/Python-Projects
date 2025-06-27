from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

app = Flask(__name__)

# ChatBot setup
Bot = ChatBot(
    name='Calculator',
    read_only=True,
    logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
    storage_adapter="chatterbot.storage.SQLStorageAdapter"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["message"]
    try:
        response = Bot.get_response(user_input)
        return jsonify({"response": str(response)})
    except:
        return jsonify({"response": "Please enter a valid input."})

if __name__ == '__main__':
    app.run(debug=True)
