import os
import requests

API_KEY = os.getenv("GROQ_API_KEY")

def analyze_resume(resume_text):

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Analyze this resume and give:
    1. Resume score out of 100
    2. Key skills detected
    3. Improvements needed

    Resume:
    {resume_text}
    """

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=payload)

    data = response.json()

    # Debug print
    print(data)

    if "choices" not in data:
        return f"API Error: {data}"

    return data["choices"][0]["message"]["content"]