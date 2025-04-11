import subprocess
import speech_recognition as sr
import pyttsx3

# Initialize TTS engine (optional)
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 160)

# Function to use Text-to-Speech (optional for feedback)
def speak_text(text):
    print(f"\n🤖 Bot: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to transcribe voice input
def transcribe_audio():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("\n🎤 Speak now... (Speak and pause to finish)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    print("✅ Audio recorded. Transcribing...")
    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("❌ Could not connect to the speech recognition service.")
        return ""

# Function used by Flask to get response from Ollama
def generate_response(user_input=None):
    if not user_input:
        user_input = transcribe_audio()
        if not user_input:
            return "Sorry, I didn’t catch that. Could you say it again?"

    try:
        prompt = f"You are a helpful and empathetic health assistant. Respond in a friendly and informative tone to: \"{user_input}\""

        result = subprocess.run(
            ['ollama', 'run', 'llama2', prompt],
            capture_output=True,
            text=True
        )

        response = result.stdout.strip()

        if not response:
            return "I'm here to help, but I need a bit more information."

        return response

    except Exception as e:
        return f"⚠️ Error while generating response: {str(e)}"
