import time
import random
import schedule
from rpi_ws281x import Adafruit_NeoPixel, Color


# LED strip configuration:
LED_COUNT      = 64      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()
####################################################################

# PULSE LIGHT
def pulse():
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 255))
        strip.setPixelColor(i - 1, Color(0, 0, 200))
        strip.setPixelColor(i - 2, Color(0, 0, 150))
        strip.setPixelColor(i - 3, Color(0, 0, 100))
        strip.setPixelColor(i - 4, Color(0, 0, 0))
        strip.show()
        time.sleep(0.1)


# TURN LIGHT RED
def red():
    print('red light')
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(255, 0, 0))
    strip.show()


# TURN LIGHT GREEN
def green():
    print('green light')
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(0, 255, 0))
    strip.show()


# TURN LIGHT BLUE
def blue():
    print('blue light')
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 255))
    strip.show()


def clear():
    print('clearing LED')
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()


def stickman():
    print('Stickman show.')
    pixels = [16, 19, 25, 27, 29, 30, 31, 34, 35, 36, 37, 39, 41, 43, 45, 46, 47, 48, 51]
    for i in pixels:
        strip.setPixelColor(i, Color(0, 0, 255))
    strip.show()


def smiley():
    print('Smiley show.')
    pixels = [16, 9, 2, 3, 4, 5, 14, 23, 31, 39, 47, 54, 61, 60, 59, 58, 49, 40, 32, 24, 21, 45, 19, 26, 34, 43]
    for i in pixels:
        strip.setPixelColor(i, Color(150, 0, 150))
        time.sleep(.1)
        strip.show()


class SchoolSchedule:
    def __init__(self):
        self.class_time = False

    def is_class_soon(self):
        self.class_time = False
        clear()
        pulse()
        smiley()
        time.sleep(300)
        clear()
        pulse()
        stickman()
        time.sleep(300)
        clear()
        pulse()
        blue()
        print('It is class time soon!')

    def is_class_time(self):
        # TURN DISPLAY GREEN
        self.class_time = True
        clear()
        time.sleep(1)
        smiley()
        time.sleep(5)
        clear()
        pulse()
        green()
        print('It is class time!')

    def not_class_time(self):
        # TURN DISPLAY BLUE
        self.class_time = False
        clear()
        time.sleep(1)
        stickman()
        time.sleep(5)
        clear()
        pulse()
        blue()
        print('It is not class time.')

    def school_out(self):
        # TURN OFF DISPLAY
        self.class_time = False
        pulse()
        clear()
        smiley()
        print('School is out for the day!')

    print('School Schedule Class inititated........')
    pulse()
    clear()

print('creating school schedule and calling it a')

a = SchoolSchedule()

print('Initializing schedule details in schedule_day()')

def schedule_day():
    # MONDAY
    # PRE CLASS
    schedule.every().monday.at('08:00').do(a.is_class_soon)
    # FIRST PERIOD
    schedule.every().monday.at('08:19').do(a.is_class_time)
    schedule.every().monday.at('10:08').do(a.not_class_time)
    # SECOND PERIOD
    schedule.every().monday.at('10:26').do(a.is_class_time)
    schedule.every().monday.at('12:18').do(a.not_class_time)
    # THIRD PERIOD
    schedule.every().monday.at('13:05').do(a.is_class_time)
    schedule.every().monday.at('13:46').do(a.not_class_time)
    # FOURTH PERIOD
    schedule.every().monday.at('13:49').do(a.is_class_time)
    schedule.every().monday.at('14:29').do(a.not_class_time)
    # FIFTH PERIOD
    schedule.every().monday.at('14:32').do(a.is_class_time)
    schedule.every().monday.at('15:13').do(a.not_class_time)
    # POST CLASS
    schedule.every().monday.at('16:00').do(a.school_out)

    # TUESDAY
    # PRE CLASS
    schedule.every().tuesday.at('08:00').do(a.is_class_soon)
    # FIRST PERIOD
    schedule.every().tuesday.at('08:19').do(a.is_class_time)
    schedule.every().tuesday.at('10:08').do(a.not_class_time)
    # SECOND PERIOD
    schedule.every().tuesday.at('10:26').do(a.is_class_time)
    schedule.every().tuesday.at('12:18').do(a.not_class_time)
    # THIRD PERIOD
    schedule.every().tuesday.at('13:05').do(a.is_class_time)
    schedule.every().tuesday.at('13:46').do(a.not_class_time)
    # FOURTH PERIOD
    schedule.every().tuesday.at('13:49').do(a.is_class_time)
    schedule.every().tuesday.at('14:29').do(a.not_class_time)
    # FIFTH PERIOD
    schedule.every().tuesday.at('14:32').do(a.is_class_time)
    schedule.every().tuesday.at('15:13').do(a.not_class_time)
    # POST CLASS
    schedule.every().tuesday.at('16:00').do(a.school_out)

    # WEDNESDAY
    # PRE CLASS
    schedule.every().wednesday.at('08:00').do(a.is_class_soon)
    # FIRST PERIOD
    schedule.every().wednesday.at('08:19').do(a.is_class_time)
    schedule.every().wednesday.at('09:12').do(a.not_class_time)
    # SECOND PERIOD
    schedule.every().wednesday.at('09:16').do(a.is_class_time)
    schedule.every().wednesday.at('10:09').do(a.not_class_time)
    # THIRD PERIOD
    schedule.every().wednesday.at('10:25').do(a.is_class_time)
    schedule.every().wednesday.at('11:22').do(a.not_class_time)
    # FOURTH PERIOD
    schedule.every().wednesday.at('11:25').do(a.is_class_time)
    schedule.every().wednesday.at('12:18').do(a.not_class_time)
    # FIFTH PERIOD
    schedule.every().wednesday.at('13:06').do(a.is_class_time)
    schedule.every().wednesday.at('13:33').do(a.not_class_time)
    # POST CLASS
    schedule.every().wednesday.at('15:00').do(a.school_out)

    # THURSDAY
    # PRE CLASS
    schedule.every().thursday.at('08:00').do(a.is_class_soon)
    # FIRST PERIOD
    schedule.every().thursday.at('08:19').do(a.is_class_time)
    schedule.every().thursday.at('10:09').do(a.not_class_time)
    # SECOND PERIOD
    schedule.every().thursday.at('10:26').do(a.is_class_time)
    schedule.every().thursday.at('12:18').do(a.not_class_time)
    # THIRD PERIOD
    schedule.every().thursday.at('13:05').do(a.is_class_time)
    schedule.every().thursday.at('13:46').do(a.not_class_time)
    # FOURTH PERIOD
    schedule.every().thursday.at('13:50').do(a.is_class_time)
    schedule.every().thursday.at('14:29').do(a.not_class_time)
    # FIFTH PERIOD
    schedule.every().thursday.at('14:32').do(a.is_class_time)
    schedule.every().thursday.at('15:12').do(a.not_class_time)
    # POST CLASS
    schedule.every().thursday.at('16:00').do(a.school_out)

    # FRIDAY
    # PRE CLASS
    schedule.every().friday.at('08:00').do(a.is_class_soon)
    # FIRST PERIOD
    schedule.every().friday.at('08:19').do(a.is_class_time)
    schedule.every().friday.at('10:09').do(a.not_class_time)
    # SECOND PERIOD
    schedule.every().friday.at('10:26').do(a.is_class_time)
    schedule.every().friday.at('12:18').do(a.not_class_time)
    # THIRD PERIOD
    schedule.every().friday.at('13:05').do(a.is_class_time)
    schedule.every().friday.at('13:46').do(a.not_class_time)
    # FOURTH PERIOD
    schedule.every().friday.at('13:50').do(a.is_class_time)
    schedule.every().friday.at('14:29').do(a.not_class_time)
    # FIFTH PERIOD
    schedule.every().friday.at('14:32').do(a.is_class_time)
    schedule.every().friday.at('15:12').do(a.not_class_time)
    # POST CLASS
    schedule.every().friday.at('16:00').do(a.school_out)

print('Schedule details in schedule_day() initialized.')

schedule_day()

print('Called schedule_day() function.')
time.sleep(.1)
print('Starting while loop to run_pending.')

while True:
    schedule.run_pending()

