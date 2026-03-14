import os
import webbrowser
import psutil

def run_command(cmd):

    if "open youtube" in cmd:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    if "open google" in cmd:
        webbrowser.open("https://google.com")
        return "Opening Google"

    if "shutdown computer" in cmd:
        os.system("shutdown /s /t 5")
        return "Shutting down system"

    if "system status" in cmd:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        return f"CPU usage {cpu} percent. RAM usage {ram} percent"

    return None
