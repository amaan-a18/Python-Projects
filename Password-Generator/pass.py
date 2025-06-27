from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

def generate_password(length):
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    s = list(s1 + s2 + s3 + s4)
    random.shuffle(s)
    return ''.join(s[:length])

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        if length >= 4:
            password = generate_password(length)
        else:
            password = "Length must be at least 4 characters."
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
