# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)

# API_KEY = "api_key"  # <-- put your Gemini API key here

# @app.route("/")
# def home():
#     return "API is running 🚀"

# @app.route("/analyze", methods=["POST"])
# def analyze():
#     try:
#         data = request.json
#         resume_text = data.get("text", "")

#         if not resume_text:
#             return jsonify({"error": "No resume text provided"}), 400

#         url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"

#         payload = {
#             "contents": [
#                 {
#                     "parts": [
#                         {
#                             "text": f"Analyze this resume:\n{resume_text}\nGive summary, skills, and improvements."
#                         }
#                     ]
#                 }
#             ]
#         }

#         response = requests.post(url, json=payload)
#         result = response.json()
#         print(result)

#         # Extract only useful text
#         output_text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response")

#         return jsonify({
#             "analysis": output_text
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     # 🔥 FIX: disable reloader to stop infinite restart issue
#     app.run(debug=True, use_reloader=False, port=3000)


# -------------------- by the help google api key config information --------------------------------------

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "api_key"

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        resume_text = data.get("text", "")

        if not resume_text:
            return jsonify({"error": "No resume text provided"}), 400

        url = f"https://aiplatform.googleapis.com/v1/publishers/google/models/gemini-2.5-flash-lite:generateContent?key={API_KEY}"

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            # ✅ resume_text is used INSIDE function
                            "text": f"Analyze this resume:\n{resume_text}\nGive summary, skills, and improvements."
                        }
                    ]
                }
            ]
        }

        response = requests.post(url, json=payload)
        result = response.json()

        output_text = result["candidates"][0]["content"]["parts"][0]["text"]

        return jsonify({"analysis": output_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=3000)
    
    
# ----------------------------- running and testing method ----------------------------------------
# curl -X POST http://127.0.0.1:3000/analyze -H "Content-Type: application/json" -d "{\"text\":\"Python developer with React and SQL experience\"}"