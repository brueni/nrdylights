#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40)

pwm.setPWMFreq(60)

#with open("scenes-static/test.scn", "r") as scene:
#    array = []
#    for line in scene:
#        array.append(line)

array = open('scenes-static/test.scn').read().split('\n')

#print array[2]
ch1 = int(array[0])
ch2 = int(array[1])
ch3 = int(array[2])

#print test 
pwm.setPWM(5, 0, ch1)
pwm.setPWM(6, 0, ch2)
pwm.setPWM(7, 0, ch3)

