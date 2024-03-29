```This README was generated by AI```
# Hermes:
This is a Python-based project for a voice-controlled bot. The bot uses speech recognition to detect user input via microphone, processes the input, and provides appropriate responses. The bot comes with multiple commands such as playing songs, providing time and day. Users can easily add more commands based on their use case.

# Setup Guide:
To set up and run this project, follow these steps:
1. Install Python 3 or above on your computer.
2. Install the necessary libraries by running the command "pip install speechrecognition pyttsx3 threading wikipedia" in a command prompt/terminal.
3. Clone or download the project's repository onto your local machine.
4. Open the "Core.py" file in a Python editor or IDE of your choice.
5. Run the file, and permit the program to access the microphone if asked.
6. The bot will start detecting your command. To invoke the bot, say "Hermes" followed by any command (such as "play a song" or "what is the time").
7. The bot will process the command and respond accordingly.

# List of Commands:
The following commands are available by default:
- play a song
- what is the time
- what day is it

Users can add more commands by creating a new Python file in the "commands" directory and implementing the "Command" class.
