from voice import speak, listen
from commands import run_command
from brain import ask_ai
from config import WAKE_WORD

def activate():

    speak("Project Jarvis Activated")

    while True:

        command = listen()

        if WAKE_WORD in command:

            speak("Yes, how can I help?")

            query = listen()

            result = run_command(query)

            if result:
                speak(result)

            else:
                answer = ask_ai(query)
                speak(answer)

if __name__ == "__main__":
    activate()
