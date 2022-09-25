import datetime
from commands.Command import Command

class Time_Command(Command):
    def __init__(self):
        self.triggers = ['time', 'hour']
        super().__init__(self.triggers)

    def call(self, text):
        time = datetime.datetime.now().strftime('%I:%M %p')
        return time
