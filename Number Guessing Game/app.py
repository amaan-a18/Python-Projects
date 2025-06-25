from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            lower = int(request.form.get("lower"))
            upper = int(request.form.get("upper"))
            difficulty = request.form.get("difficulty")

            if lower >= upper:
                return render_template("index.html", game_started=False, error="Lower bound must be less than upper bound.")

            session["lower"] = lower
            session["upper"] = upper
            session["number"] = random.randint(lower, upper)
            session["chances"] = 10 if difficulty == "easy" else 5
            session["guesses"] = []
            session["message"] = ""
            session["game_over"] = False
            return redirect(url_for("game"))

        except ValueError:
            return render_template("index.html", game_started=False, error="Please enter valid numeric bounds.")

    return render_template("index.html", game_started=False)

@app.route("/game", methods=["GET", "POST"])
def game():
    if "number" not in session:
        return redirect(url_for("index"))

    if request.method == "POST" and not session.get("game_over", False):
        try:
            guess = int(request.form.get("guess"))
            session["guesses"].append(guess)
            session["chances"] -= 1
            number = session["number"]

            if guess == number:
                session["message"] = f"🎉 Correct! The number was {number}."
                session["game_over"] = True
            elif session["chances"] == 0:
                session["message"] = f"💥 Game Over! The number was {number}."
                session["game_over"] = True
            elif guess < number:
                session["message"] = "🔼 Too Low!"
            else:
                session["message"] = "🔽 Too High!"
        except:
            session["message"] = "Please enter a valid number."

    return render_template("index.html",
                           game_started=True,
                           chances=session["chances"],
                           guesses=session["guesses"],
                           lower=session["lower"],
                           upper=session["upper"],
                           message=session["message"],
                           game_over=session["game_over"])

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
