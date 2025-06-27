from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)
url_map = {}

def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        original_url = request.form.get('original_url')
        short_id = generate_short_id()
        while short_id in url_map:
            short_id = generate_short_id()
        url_map[short_id] = original_url
        short_url = request.host_url + short_id
    return render_template('index.html', short_url=short_url)

@app.route('/<short_id>')
def redirect_url(short_id):
    original_url = url_map.get(short_id)
    if original_url:
        return redirect(original_url)
    return "<h1>🔍 URL Not Found</h1>", 404

if __name__ == "__main__":
    app.run(debug=True)
