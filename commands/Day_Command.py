import datetime
import calendar

from commands.Command import Command 

class Day_Command(Command):
    def __init__(self):
        self.triggers = ['day', 'date']
        super().__init__(self.triggers)

    def call(self, text):
        day_of_the_week = datetime.datetime.today().weekday()
        week_day = calendar.day_name[day_of_the_week]

        day_of_the_month = datetime.datetime.now().strftime("%d")

        month_day = ""
        if (day_of_the_month == '1'):
            month_day = "1st"
        elif (day_of_the_month == '2'):
            month_day = "2nd"
        elif (day_of_the_month == '3'):
            month_day = "3rd"
        elif (day_of_the_month == '21'):
            month_day = "21st"
        elif (day_of_the_month == '22'):
            month_day = "22nd"
        elif (day_of_the_month == '23'):
            month_day = "23rd"
        elif (day_of_the_month == '31'):
            month_day = "31st"
        else:
            month_day = (str(day_of_the_month) + "th")

        return week_day + " the " + month_day
