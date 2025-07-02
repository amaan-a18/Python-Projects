from flask import Flask, render_template, request, redirect, url_for
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_created = False
    if request.method == "POST":
        link = request.form.get("url")

        if link:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")
            
            img_path = os.path.join("static", "qrcode.jpg")
            img.save(img_path)
            qr_created = True

    return render_template("index.html", qr_created=qr_created)

if __name__ == "__main__":
    app.run(debug=True)
