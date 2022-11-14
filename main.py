import time
import datetime


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday']
periods = {0: {1: {'start': '8:20', 'end': '10:10'},
               2: {'start': '10:29', 'end': '12:20'},
               3: {'start': '1:08', 'end': '1:48'},
               4: {'start': '1:51', 'end': '2:31'},
               5: {'start': '2:34', 'end': '3:15'}},

           0: {1: {'start': '8:20', 'end': '10:10'},
               2: {'start': '10:29', 'end': '12:20'},
               3: {'start': '1:08', 'end': '1:48'},
               4: {'start': '1:51', 'end': '2:31'},
               5: {'start': '2:34', 'end': '3:15'}},

           2: {1: {'start': '8:20', 'end': '9:14'},
               2: {'start': '9:17', 'end': '10:10'},
               3: {'start': '10:29', 'end': '11:23'},
               4: {'start': '11:26', 'end': '12:20'},
               5: {'start': '1:08', 'end': '1:35'}},

           3: {1: {'start': '8:20', 'end': '10:10'},
               2: {'start': '10:29', 'end': '12:20'},
               3: {'start': '1:08', 'end': '1:48'},
               4: {'start': '1:51', 'end': '2:31'},
               5: {'start': '2:34', 'end': '3:15'}},

           1: {1: {'start': '8:20', 'end': '10:10'},
               2: {'start': '10:29', 'end': '12:20'},
               3: {'start': '1:08', 'end': '1:48'},
               4: {'start': '1:51', 'end': '2:31'},
               5: {'start': '07:58', 'end': '07:59'}}}

class_time = True


# TURN LIGHT RED
def red():
    print('red light')
    pass


# TURN LIGHT GREEN
def green():
    print('green light')
    pass


# TURN LIGHT BLUE
def blue():
    print('blue light')
    pass


while True:
    now = datetime.datetime.now()
    hour_minute = now.strftime("%I:%M")

    if class_time:
        print('IT IS CLASS TIME')
        green()
    else:
        print('IT IS NOT CLASS TIME')
        blue()

    for period in periods[now.weekday()]:

        class_start = periods[now.weekday()][period]['start']
        class_end = periods[now.weekday()][period]['end']

        if class_time:
            pass
        else:
            if hour_minute == class_start:
                class_time = True
                green()
                time.sleep(1)
                red()
                time.sleep(1)
                green()
                time.sleep(1)
                red()
                time.sleep(1)
        if not class_time:
            pass
        else:
            if hour_minute == class_end:
                class_time = False
                blue()
                time.sleep(1)
                red()
                time.sleep(1)
                blue()
                time.sleep(1)
                red()
                time.sleep(1)




