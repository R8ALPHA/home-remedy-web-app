from flask import Flask, render_template, request
from remedies import remedies

app = Flask(__name__)

def find_remedy(user_input):
    user_input = user_input.lower()

    for problem in remedies:
        if problem in user_input:
            return remedies[problem]

    return None

@app.route("/", methods=["GET", "POST"])
def index():
    remedy = None

    if request.method == "POST":
        problem_input = request.form["problem"].strip().lower()
        remedy = find_remedy(problem_input)

    return render_template("index.html", remedy=remedy)

if __name__ == "__main__":
    app.run(debug=True)
