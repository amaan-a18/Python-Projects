from flask import Flask, render_template, request
import random

app = Flask(__name__)

DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "protonmail.com"]

def generate_email(first, last, domain):
    number = random.randint(10, 9999)
    return f"{first.lower()}.{last.lower()}{number}@{domain}"

@app.route('/', methods=['GET', 'POST'])
def index():
    emails = []
    if request.method == 'POST':
        first = request.form.get('first_name', '').strip()
        last = request.form.get('last_name', '').strip()
        domain = request.form.get('domain', 'gmail.com')
        count = request.form.get('count', '1')
        
        if first and last and count.isdigit():
            for _ in range(min(int(count), 20)):  # Limit max generation to 20
                emails.append(generate_email(first, last, domain))
        else:
            emails.append("Please fill all fields correctly.")
    
    return render_template('index.html', emails=emails, domains=DOMAINS)

if __name__ == '__main__':
    app.run(debug=True)
