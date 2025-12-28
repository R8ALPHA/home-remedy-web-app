from flask import Flask, render_template, request
from remedies import remedies

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        problem = request.form["problem"].lower()
        result = remedies.get(problem)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
