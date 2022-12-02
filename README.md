# rgb-led
Raspi Hat LED 8x8 class indicator project

I wanted a classroom indicator that students could easily understand, regarding when class starts and when class is over. There is no school bell. I used a raspberry pi zero w, with an 8x8 RGB LED hat, controlled by python.

The library to control the raspberry pi LED hat is rpi_ws2812.
The library to control the scheduling is schedule.

second.py is the functioning code. 
LED turns green when class is in.
LED turns blue when class is out.
LED pulses, draws smiley face and stick figure in between these two states. 

Within 2 days students have already started reacting to the LED indicator; the question of 'when is class over', has been dramatically reduced.
