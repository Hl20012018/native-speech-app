from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
from groq import Groq
from groq import Groq
load_dotenv()

app = Flask(__name__)

client = Groq(
  api_key=os.getenv("API_KEY")
)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        text = request.form["text"]
        emotion = request.form["emotion"]

        prompt = f"""
Rewrite this sentence exactly how a native American speaker would naturally say it.

Emotion:
{emotion}

Rules:
- Make it sound natural
- Use native American phrasing
- Show speech melody using UPPERCASE where the voice stresses words
- Lowercase where speech relaxes
- Return ONLY the final sentence
- No explanations

Sentence:
{text}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)