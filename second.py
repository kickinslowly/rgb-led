import time
import datetime
import random
import schedule
#
# # TURN LIGHT RED
# def red():
#     print('red light')
#     pass
#
#
# # TURN LIGHT GREEN
# def green():
#     print('green light')
#     pass
#
#
# # TURN LIGHT BLUE
# def blue():
#     print('blue light')
#     pass
#

class SchoolSchedule:
    def __init__(self):
        self.class_time = False

    def is_class_soon(self):
        # DISPLAY NUMBER OF MINUTES UNTIL CLASS
        # OR MAYBE PULSE
        self.class_time = False
        print('It is class time soon!')

    def is_class_time(self):
        # TURN DISPLAY GREEN
        self.class_time = True
        print('It is class time!')

    def not_class_time(self):
        # TURN DISPLAY BLUE
        self.class_time = False
        print('It is not class time.')

    def school_out(self):
        # TURN OFF DISPLAY
        self.class_time = False
        print('School is out for the day!')


    print('School Schedule inititated........')


a = SchoolSchedule()


def schedule_day(day):
    if day == 'monday' or day == 'tuesday' or day == 'thursday' or day == 'friday':
        # PRE CLASS
        schedule.every().day.at('08:00').do(a.is_class_soon)
        # FIRST PERIOD
        schedule.every().day.at('08:19').do(a.is_class_time)
        schedule.every().day.at('10:09').do(a.not_class_time)
        # SECOND PERIOD
        schedule.every().day.at('10:28').do(a.is_class_time)
        schedule.every().day.at('12:18').do(a.not_class_time)
        # THIRD PERIOD
        schedule.every().day.at('13:07').do(a.is_class_time)
        schedule.every().day.at('13:47').do(a.not_class_time)
        # FOURTH PERIOD
        schedule.every().day.at('13:50').do(a.is_class_time)
        schedule.every().day.at('14:30').do(a.not_class_time)
        # FIFTH PERIOD
        schedule.every().day.at('14:33').do(a.is_class_time)
        schedule.every().day.at('15:13').do(a.not_class_time)
        # POST CLASS
        schedule.every().day.at('16:00').do(a.school_out)
    else:
        # PRE CLASS
        schedule.every().day.at('08:00').do(a.is_class_soon)
        # FIRST PERIOD
        schedule.every().day.at('08:19').do(a.is_class_time)
        schedule.every().day.at('09:13').do(a.not_class_time)
        # SECOND PERIOD
        schedule.every().day.at('09:16').do(a.is_class_time)
        schedule.every().day.at('10:09').do(a.not_class_time)
        # THIRD PERIOD
        schedule.every().day.at('10:28').do(a.is_class_time)
        schedule.every().day.at('11:22').do(a.not_class_time)
        # FOURTH PERIOD
        schedule.every().day.at('11:25').do(a.is_class_time)
        schedule.every().day.at('12:18').do(a.not_class_time)
        # FIFTH PERIOD
        schedule.every().day.at('13:07').do(a.is_class_time)
        schedule.every().day.at('13:33').do(a.not_class_time)
        # POST CLASS
        schedule.every().day.at('16:00').do(a.school_out)


schedule_day('monday')
schedule_day('tuesday')
schedule_day('wednesday')
schedule_day('thursday')
schedule_day('friday')

while True:
    schedule.run_pending()

