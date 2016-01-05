#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time, sys

pwm = PWM(0x40)

pwm.setPWMFreq(120)

#define Channels, r=red b=blue g=green
ch1r = 1
ch1g = 2
ch1b = 0
ch2r = 4
ch2g = 3
ch2b = 8
ch3r = 5
ch3g = 7
ch3b = 6
ch4r = 10
ch4g = 11
ch4b = 9
ch5r = 13
ch5g = 12
ch5b = 14

#read Scene-File into array
array = open('scenes-static/test.scn').read().split('\n')

#put array-values into vars
val1r = int(array[0])
val1g = int(array[1])
val1b = int(array[2])
val2r = int(array[3])
val2g = int(array[4])
val2b = int(array[5])
val3r = int(array[6])
val3g = int(array[7])
val3b = int(array[8])
val4r = int(array[9])
val4g = int(array[10])
val4b = int(array[11])
val5r = int(array[12])
val5g = int(array[13])
val5b = int(array[14])

#set all channels to values
pwm.setPWM(ch1r, 0, val1r)
pwm.setPWM(ch1g, 0, val1g)
pwm.setPWM(ch1b, 0, val1b)
pwm.setPWM(ch2r, 0, val2r)
pwm.setPWM(ch2g, 0, val2g)
pwm.setPWM(ch2b, 0, val2b)
pwm.setPWM(ch3r, 0, val3r)
pwm.setPWM(ch3g, 0, val3g)
pwm.setPWM(ch3b, 0, val3b)
pwm.setPWM(ch4r, 0, val4r)
pwm.setPWM(ch4g, 0, val4g)
pwm.setPWM(ch4b, 0, val4b)
pwm.setPWM(ch5r, 0, val5r)
pwm.setPWM(ch5g, 0, val5g)
pwm.setPWM(ch5b, 0, val5b)


time.sleep(3)

i = 0
while i <= 14:
	pwm.setPWM(i, 0, 0)
	i = i + 1

#print sys.argv[1]
