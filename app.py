from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend Running ✅"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    text = data.get("text", "")

    if "fake" in text.lower():
        return jsonify({
            "result": "Fake",
            "confidence": 0.85
        })
    else:
        return jsonify({
            "result": "Real",
            "confidence": 0.90
        })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)