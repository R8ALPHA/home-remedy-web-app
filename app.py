from flask import Flask, render_template, request

app = Flask(__name__)

remedies = [
    {
        "keywords": ["cold", "common cold", "runny nose", "blocked nose", "sneezing"],
        "steps": [
            "Drink warm water frequently.",
            "Have ginger or tulsi tea.",
            "Inhale steam twice a day.",
            "Take proper rest."
        ]
    },
    {
        "keywords": ["cough", "dry cough", "wet cough"],
        "steps": [
            "Drink warm honey and ginger water.",
            "Avoid cold foods and drinks.",
            "Gargle with warm salt water."
        ]
    },
    {
        "keywords": ["fever", "high temperature", "temperature"],
        "steps": [
            "Drink plenty of fluids.",
            "Rest as much as possible.",
            "Apply a cold compress on the forehead."
        ]
    },
    {
        "keywords": ["headache", "head pain", "migraine"],
        "steps": [
            "Rest in a quiet, dark room.",
            "Drink enough water.",
            "Apply a cold or warm compress."
        ]
    },
    {
        "keywords": ["sore throat", "throat pain", "throat infection"],
        "steps": [
            "Gargle with warm salt water.",
            "Drink warm fluids.",
            "Avoid very cold foods."
        ]
    },
    {
        "keywords": ["stomach ache", "stomach pain", "abdominal pain"],
        "steps": [
            "Drink warm water.",
            "Apply a warm compress to the stomach.",
            "Eat light and simple food."
        ]
    },
    {
        "keywords": ["acidity", "acid reflux", "heartburn"],
        "steps": [
            "Drink cold milk.",
            "Avoid spicy foods.",
            "Eat small meals."
        ]
    },
    {
        "keywords": ["diarrhea", "loose motions"],
        "steps": [
            "Drink ORS or salted water.",
            "Eat plain foods like rice and banana.",
            "Avoid oily foods."
        ]
    },
    {
        "keywords": ["constipation"],
        "steps": [
            "Drink plenty of water.",
            "Eat fiber-rich foods.",
            "Exercise lightly."
        ]
    },
    {
        "keywords": ["toothache", "tooth pain"],
        "steps": [
            "Rinse mouth with warm salt water.",
            "Apply clove oil on the affected tooth.",
            "Avoid very hot or cold food."
        ]
    },
    {
        "keywords": ["burn", "minor burn"],
        "steps": [
            "Hold the burned area under cool running water.",
            "Apply aloe vera gel.",
            "Do not pop blisters."
        ]
    },
    {
        "keywords": ["cut", "minor cut", "wound"],
        "steps": [
            "Clean the wound with water.",
            "Apply antiseptic.",
            "Cover with a clean bandage."
        ]
    },
    {
        "keywords": ["nosebleed"],
        "steps": [
            "Sit upright and lean forward.",
            "Pinch the nose for 10 minutes.",
            "Apply a cold compress."
        ]
    },
    {
        "keywords": ["ear pain", "earache"],
        "steps": [
            "Apply a warm compress.",
            "Keep the ear dry.",
            "Avoid inserting objects into the ear."
        ]
    },
    {
        "keywords": ["vomiting", "nausea"],
        "steps": [
            "Sip water slowly.",
            "Eat bland foods.",
            "Rest well."
        ]
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    remedy_steps = None
    problem = ""

    if request.method == "POST":
        problem = request.form.get("problem", "").lower()

        for remedy in remedies:
            for keyword in remedy["keywords"]:
                if keyword in problem:
                    remedy_steps = remedy["steps"]
                    break
            if remedy_steps:
                break

    return render_template("index.html", remedy_steps=remedy_steps, problem=problem)

if __name__ == "__main__":
    app.run(debug=True)
