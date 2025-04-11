# Hack-Byte
# HealthCare

# 🩺 Smart Health Assistant – AI-Powered Virtual Doctor (Offline & Voice Enabled)

A complete AI-powered health assistant designed for rural and low-resource areas. This web app integrates symptom analysis, mental health checkups, voice-based interactions, and offline AI-powered responses—all running locally using open-source models like *LLaMA2* via *Ollama*.

---

## 🚀 Project Overview

### 🌟 What We Aim to Solve:
Millions in rural and underserved communities lack access to timely healthcare and digital literacy. Our goal is to:
- Promote regular medical checkups 🩺
- Offer 24/7 accessible health guidance 💬
- Empower users through voice-driven interaction 🗣
- Ensure privacy with offline, local AI support 🔐

---

## 🧠 Key Features

- *🧾 Doctor Visit Logger*: Store and view doctor visits with date and notes
- *⚠ Smart Health Alerts*: Auto-alerts based on symptoms like fever or pain
- *💡 Rotating Health Tips*: Simple daily prevention tips
- *🧠 Mental Health Checkup*: Empathetic analysis using LLaMA2 via Ollama
- *👨‍⚕ Virtual AI Doctor*: Voice-enabled chatbot with local LLM (LLaMA2)
- *✅ Checklist Before Visiting Doctor*: Static checklist for preparation
- *📌 Health FAQs*: Rotating FAQ section to guide users

---

## 🛠 Tech Stack

- *Frontend*: HTML5, CSS3, JavaScript
- *Backend*: Python, Flask
- *AI Models*: LLaMA2 (via Ollama), running locally
- *Voice Engine*: pyttsx3 for Text-to-Speech
- *Speech Input*: Web speech recognition
- *Others*: Bootstrap, jQuery, Flask-CORS

---

## 🖥 How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/health-assistant.git
cd health-assistant


Setup Python Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Run the Flask App
python app.py


Ensure Ollama & LLaMA2 are Installed
Make sure Ollama is installed and you’ve pulled the LLaMA2 model:
ollama run llama2
