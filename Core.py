import speech_recognition as sr
import pyttsx3
import threading
import wikipedia

from commands.Command import Command
from commands.Play_Command import Play_Command
from commands.Time_Command import Time_Command
from commands.Day_Command import Day_Command

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

commands = [
    Time_Command(),
    Play_Command(),
    Day_Command()
]

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'hermes' in command:
                command = command.replace('hermes', '')
                print(command)
    except:
        return ""
    return command

def run_hermes():
    command = take_command()
    if command == "":
        pass
    else:
        for cmd in commands:
            for word in cmd.triggers:
                if word in command:
                    talk(cmd.call(command))
                    print("Command Completed")

while True:
    run_hermes()