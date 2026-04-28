import requests
import json

# Replace with your NEW Gemini API key
API_KEY = "your_api_key"

# Updated working free-tier model
MODEL = "gemini-2.5-flash"

url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Reply with only this text: Gemini API working successfully"
                }
            ]
        }
    ]
}

try:
    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=30
    )

    print("Status Code:", response.status_code)
    print("Response:")
    print(json.dumps(response.json(), indent=2))

except Exception as e:
    print("Error:", str(e))