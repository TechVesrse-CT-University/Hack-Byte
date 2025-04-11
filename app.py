from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pyttsx3
import subprocess
import pandas as pd
import pickle
import numpy as np

from chatbot import generate_response

app = Flask(__name__)
CORS(app)

doctor_visits = []
interactions = []

@app.route("/", methods=["GET", "POST"])
def index():
    alert = ""
    health_tips = [
        "Drink clean water to prevent diseases.",
        "Use mosquito nets to avoid malaria and dengue.",
        "Wash hands regularly to prevent infections.",
        "Eat fresh fruits and vegetables daily."
    ]

    if request.method == "POST":
        name = request.form.get("name")
        date = request.form.get("date")
        notes = request.form.get("notes")

        if name and date:
            doctor_visits.append({"name": name, "date": date, "notes": notes})

        if notes and ("fever" in notes.lower() or "pain" in notes.lower()):
            alert = "⚠️ You should see a doctor!"

    return render_template("index.html", visits=doctor_visits, alert=alert, tips=health_tips)

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.json
    user_input = data.get("user_input")
    response = generate_response(user_input)

    interactions.append({
        "user": user_input,
        "assistant": response
    })

    return jsonify({"response": response})

# ------------------------------
# ✅ MENTAL HEALTH CHECKUP (with LLaMA2)
# ------------------------------
@app.route("/check_mental_health", methods=["POST"])
def check_mental_health():
    try:
        user_input = request.json
        age = user_input.get("age")
        gender = user_input.get("gender")
        work_stress = user_input.get("work_stress")
        sleep_issues = user_input.get("sleep_issues")
        support = user_input.get("support")

        prompt = f"""
        A user filled a mental health checkup form with the following information:
        - Age: {age}
        - Gender: {gender}
        - Work-related stress: {work_stress}
        - Trouble sleeping: {sleep_issues}
        - Emotional support from friends/family: {support}

        Based on this, provide a short, empathetic mental health analysis and a helpful suggestion.
        """

        result = subprocess.run(
            ["ollama", "run", "llama2"],
            input=prompt,
            text=True,
            capture_output=True
        )

        llm_response = result.stdout.strip()
        return jsonify({"result": llm_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------
# ✅ VIRTUAL MENTAL DOCTOR (TTS + LLaMA2)
# ------------------------------
def get_doctor_response(user_input):
    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama2'],
            input=user_input.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30
        )

        response = result.stdout.decode('utf-8').strip()
        if not response:
            response = "Sorry, I couldn't understand that. Can you try rephrasing?"

        return response
    except subprocess.TimeoutExpired:
        return "The response took too long. Please try again later."
    except Exception as e:
        return f"Error: {str(e)}"

def speak_response(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    engine.save_to_file(text, "static/response.mp3")
    engine.runAndWait()

@app.route('/ask_doctor', methods=['POST'])
def ask_virtual_doctor():
    try:
        user_question = request.json['question']
        answer = get_doctor_response(user_question)
        speak_response(answer)
        return jsonify({'answer': answer, 'audio': '/static/response.mp3'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ------------------------------

if __name__ == "__main__":
    app.run(debug=True)
