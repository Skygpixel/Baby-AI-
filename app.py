from flask import Flask, request, jsonify, render_template
import pandas as pd
from fuzzywuzzy import process  # smarter string matching

app = Flask(__name__)

# 🌸 Step 1: Load dataset
df = pd.read_csv("emotions.csv")

# 🌸 Step 2: Prediction function (same as in emotions_ai.py)
def predict_emotion(feeling):
    result = process.extractOne(feeling, df["feeling"])
    if result:  # make sure something was found
        match = result[0]   # string that matched
        score = result[1]   # similarity score
        if score >= 60:
            return df[df["feeling"] == match]["emotion"].values[0]
    return "unknown"

# 🌸 Step 3: Website routes
@app.route("/")
def home():
    return render_template("index.html")  # your lavender chat page

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    feeling = data.get("feeling", "")
    emotion = predict_emotion(feeling)
    return jsonify({"emotion": emotion})

if __name__ == "__main__":
    app.run(debug=True)  # starts your website locallyg
    