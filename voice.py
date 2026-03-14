import pyttsx3
import speech_recognition as sr
from config import VOICE_RATE

engine = pyttsx3.init()
engine.setProperty('rate', VOICE_RATE)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("User:", command)
        return command.lower()

    except:
        return ""
