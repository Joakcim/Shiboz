from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)
client = genai.Client(api_key="AIzaSyB9WLMDomjXU-4lGujs9riV5iyPKUwQb7U")

@app.route("/ask", methods=["POST"])
def ask():
    prompt = request.json.get("prompt")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)
