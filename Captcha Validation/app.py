from flask import Flask, render_template, request, session, redirect, url_for
import random
import string

app = Flask(__name__)
app.secret_key = "supersecret"

def generate_captcha(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("captcha_input")
        real_captcha = session.get("captcha")

        if user_input and user_input.upper() == real_captcha:
            session["message"] = "✅ CAPTCHA Verified Successfully!"
            session["success"] = True
        else:
            session["message"] = "❌ CAPTCHA Mismatch. Please try again."
            session["success"] = False
        return redirect(url_for("index"))

    captcha = generate_captcha()
    session["captcha"] = captcha
    return render_template("index.html", captcha=captcha, message=session.pop("message", ""), success=session.pop("success", None))

if __name__ == "__main__":
    app.run(debug=True)
