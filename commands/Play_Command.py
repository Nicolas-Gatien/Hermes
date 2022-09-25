import pywhatkit
from commands.Command import Command

class Play_Command(Command):
    def __init__(self):
        self.triggers = ['play']
        super().__init__(self.triggers)

    def call(self, search):
        song = search.replace('play','')
        pywhatkit.playonyt(song)        
        return 'playing' + song
