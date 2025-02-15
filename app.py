from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# Load API Key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in environment variables")
    
genai.configure(api_key=API_KEY)

@app.route("/generate", methods=["POST"])
def generate_description():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files["image"]
        language = request.form.get("language", "en")

        image_data = image_file.read()

        response = genai.generate_content(
            model="gemini-1.5-pro",
            contents=[
                {"type": "image", "data": image_data},
                {"type": "text", "data": f"Describe this landmark in {language}."}
            ]
        )

        return jsonify({"description": response.text})

    except Exception as e:
        print("Error:", str(e))  # Logs error in Vercel logs
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
