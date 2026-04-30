from flask import Flask, request, jsonify
from flask_cors import CORS

print("Backend starting...")

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    scenario = data.get("scenario")

    # Feedback logic
    word_count = len(user_message.split())

    if word_count < 5:
        clarity = "Low"
    elif word_count < 10:
        clarity = "Medium"
    else:
        clarity = "Good"

    if scenario == "Interview":
        reply = f"[Interview Mode] You said: '{user_message}'. Can you elaborate with a real example?"
    
    elif scenario == "Presentation":
        reply = f"[Presentation Mode] '{user_message}' is a good point. Try structuring it better."
    
    elif scenario == "Casual Talk":
        reply = f"[Casual Mode] Nice! '{user_message}' sounds interesting 😊"
    
    else:
        reply = f"You said: {user_message}"

    feedback = f"Clarity: {clarity}"

    return jsonify({
        "reply": reply,
        "feedback": feedback
    })

# 🔥 THIS PART WAS MISSING
if __name__ == "__main__":
    print("Running Flask app...")
    app.run(debug=True)