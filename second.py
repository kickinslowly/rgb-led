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


def schedule_day():
    # MONDAY
    # PRE CLASS
    schedule.every().monday.at('08:00').do(a.is_class_soon)
    # FIRST PERIOD
    schedule.every().monday.at('08:19').do(a.is_class_time)
    schedule.every().monday.at('09:13').do(a.not_class_time)
    # SECOND PERIOD
    schedule.every().monday.at('09:16').do(a.is_class_time)
    schedule.every().monday.at('10:09').do(a.not_class_time)
    # THIRD PERIOD
    schedule.every().monday.at('10:28').do(a.is_class_time)
    schedule.every().monday.at('11:22').do(a.not_class_time)
    # FOURTH PERIOD
    schedule.every().monday.at('11:25').do(a.is_class_time)
    schedule.every().monday.at('12:18').do(a.not_class_time)
    # FIFTH PERIOD
    schedule.every().monday.at('13:07').do(a.is_class_time)
    schedule.every().monday.at('13:33').do(a.not_class_time)
    # POST CLASS
    schedule.every().monday.at('16:00').do(a.school_out)

    # TUESDAY
    # PRE CLASS
    schedule.every().tuesday.at('08:00').do(a.is_class_soon)
    # FIRST PERIOD
    schedule.every().tuesday.at('08:19').do(a.is_class_time)
    schedule.every().tuesday.at('09:13').do(a.not_class_time)
    # SECOND PERIOD
    schedule.every().tuesday.at('09:16').do(a.is_class_time)
    schedule.every().tuesday.at('10:09').do(a.not_class_time)
    # THIRD PERIOD
    schedule.every().tuesday.at('10:28').do(a.is_class_time)
    schedule.every().tuesday.at('11:22').do(a.not_class_time)
    # FOURTH PERIOD
    schedule.every().tuesday.at('11:25').do(a.is_class_time)
    schedule.every().tuesday.at('12:18').do(a.not_class_time)
    # FIFTH PERIOD
    schedule.every().tuesday.at('13:07').do(a.is_class_time)
    schedule.every().tuesday.at('13:33').do(a.not_class_time)
    # POST CLASS
    schedule.every().tuesday.at('16:00').do(a.school_out)

    # WEDNESDAY
    # PRE CLASS
    schedule.every().wednesday.at('17:38').do(a.is_class_soon)
    # FIRST PERIOD
    schedule.every().wednesday.at('08:19').do(a.is_class_time)
    schedule.every().wednesday.at('17:39').do(a.not_class_time)
    # SECOND PERIOD
    schedule.every().wednesday.at('10:28').do(a.is_class_time)
    schedule.every().wednesday.at('12:18').do(a.not_class_time)
    # THIRD PERIOD
    schedule.every().wednesday.at('13:07').do(a.is_class_time)
    schedule.every().wednesday.at('13:47').do(a.not_class_time)
    # FOURTH PERIOD
    schedule.every().wednesday.at('13:50').do(a.is_class_time)
    schedule.every().wednesday.at('14:30').do(a.not_class_time)
    # FIFTH PERIOD
    schedule.every().wednesday.at('14:33').do(a.is_class_time)
    schedule.every().wednesday.at('15:13').do(a.not_class_time)
    # POST CLASS
    schedule.every().wednesday.at('16:00').do(a.school_out)

    # THURSDAY
    # PRE CLASS
    schedule.every().thursday.at('08:00').do(a.is_class_soon)
    # FIRST PERIOD
    schedule.every().thursday.at('08:19').do(a.is_class_time)
    schedule.every().thursday.at('09:13').do(a.not_class_time)
    # SECOND PERIOD
    schedule.every().thursday.at('09:16').do(a.is_class_time)
    schedule.every().thursday.at('10:09').do(a.not_class_time)
    # THIRD PERIOD
    schedule.every().thursday.at('10:28').do(a.is_class_time)
    schedule.every().thursday.at('11:22').do(a.not_class_time)
    # FOURTH PERIOD
    schedule.every().thursday.at('11:25').do(a.is_class_time)
    schedule.every().thursday.at('12:18').do(a.not_class_time)
    # FIFTH PERIOD
    schedule.every().thursday.at('13:07').do(a.is_class_time)
    schedule.every().thursday.at('13:33').do(a.not_class_time)
    # POST CLASS
    schedule.every().thursday.at('16:00').do(a.school_out)

    # FRIDAY
    # PRE CLASS
    schedule.every().friday.at('08:00').do(a.is_class_soon)
    # FIRST PERIOD
    schedule.every().friday.at('08:19').do(a.is_class_time)
    schedule.every().friday.at('09:13').do(a.not_class_time)
    # SECOND PERIOD
    schedule.every().friday.at('09:16').do(a.is_class_time)
    schedule.every().friday.at('10:09').do(a.not_class_time)
    # THIRD PERIOD
    schedule.every().friday.at('10:28').do(a.is_class_time)
    schedule.every().friday.at('11:22').do(a.not_class_time)
    # FOURTH PERIOD
    schedule.every().friday.at('11:25').do(a.is_class_time)
    schedule.every().friday.at('12:18').do(a.not_class_time)
    # FIFTH PERIOD
    schedule.every().friday.at('13:07').do(a.is_class_time)
    schedule.every().friday.at('13:33').do(a.not_class_time)
    # POST CLASS
    schedule.every().friday.at('16:00').do(a.school_out)


schedule_day()

while True:
    schedule.run_pending()

