#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time, sys

pwm = PWM(0x40)

pwm.setPWMFreq(120)

from_red = 4000
from_green = 4000
from_blue = 4000
to_red = 0
to_green = 0
to_blue = 0
steps = 300
delay = 0.1
#def fade_rgb(self, from_red, from_green, from_blue, to_red, to_green, to_blue, steps, delay):
#        """Fade from one rgb value to another in steps, waiting for delay ms between each step
#            all rgb values must be 10 bit ints (between 0 and 1023)"""
red_step = float(to_red - from_red)/steps
green_step = float(to_green - from_green)/steps
blue_step = float(to_blue - from_blue)/steps
        
for step in range(0, steps+1):
	red_value = int(from_red + red_step*step)
	green_value = int(from_green + green_step*step)
	blue_value = int(from_blue + blue_step*step)
	pwm.setPWM(5, 0, green_value)
	pwm.setPWM(6, 0, blue_value)
	pwm.setPWM(7, 0, red_value)
            #self.set_rgb(red_value, green_value, blue_value)
	time.sleep(delay)


