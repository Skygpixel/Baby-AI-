# emotions_ai.py

import pandas as pd
from fuzzywuzzy import process  # smarter string matching

# 🌸 Step 1: Load dataset
df = pd.read_csv("emotions.csv")
print(f"✅ Dataset loaded with {len(df)} rows")

# 🌸 Step 2: Prediction function
def predict_emotion(feeling):
    result = process.extractOne(feeling, df["feeling"])
    if result:  # make sure something was found
        match = result[0]   # the string that matched
        score = result[1]   # similarity score
        if score >= 60:
            return df[df["feeling"] == match]["emotion"].values[0]
    return "unknown"

# 🌸 Step 3: Test predictions
print(predict_emotion("my chest feels tight"))
print(predict_emotion("I feel ugly"))
print(predict_emotion("I redo my work all the time"))
print(predict_emotion("I'm hiding from everyone"))

# 🌸 Step 4: Interactive mode
while True:
    user_input = input("\nTell me your feeling (or type 'quit'): ")
    if user_input.lower() == "quit":
        print("👋 Goodbye, take care of your feelings!")
        break
    print("Emotion:", predict_emotion(user_input))