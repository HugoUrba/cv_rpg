from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Helper function to load JSON data
def load_data(filename):
    filepath = os.path.join("data", filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    skills = load_data("skills.json")
    return render_template("profile.html", skills=skills)

@app.route("/quests")
def quests():
    quests = load_data("quests.json")
    return render_template("quests.html", quests=quests)

@app.route("/api/skills")
def api_skills():
    return jsonify(load_data("skills.json"))

@app.route("/api/quests")
def api_quests():
    return jsonify(load_data("quests.json"))

if __name__ == "__main__":
    app.run(debug=True)