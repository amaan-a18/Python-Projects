from flask import Flask, render_template, request
import requests
import bs4

app = Flask(__name__)

def verify_links(url):
    try:
        res1 = requests.get(url)
        res1.raise_for_status()
        soup = bs4.BeautifulSoup(res1.text, "html.parser")
        pageLinks = [link.get("href") for link in soup.select("a") if link.get("href")]

        results = []
        brokenCount = 0
        goodCount = 0

        for link in pageLinks:
            if link.startswith("http"):
                try:
                    res2 = requests.get(link, timeout=5)
                    res2.raise_for_status()
                    results.append(f"✅ Good: {link}")
                    goodCount += 1
                except:
                    results.append(f"❌ Broken: {link}")
                    brokenCount += 1

        results.append(f"\n🔵 {goodCount} Good | 🔴 {brokenCount} Broken")

        return results
    except Exception as e:
        return [f"🚫 Error: {e}"]

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        url = request.form["url"]
        results = verify_links(url)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
