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

#Arg1 - Static or Dynamic
scenetype = sys.argv[1]

#Arg2 - Scenefile
scenefile = sys.argv[2]

#Write Channel Function
def setchannel( channel, value ):
	pwm.setPWM(channel, 0, value)
	statefile = 'state/' + str(channel) + '.state'
	filehandle = open(statefile, "w")
	current_value = str(value)
	filehandle.write(current_value)
	filehandle.close()

#Fade-Function
def fadefromto( channel, from_red, from_green, from_blue, to_red, to_green, to_blue, steps, delay ):
	red_step = float(to_red - from_red)/steps
	green_step = float(to_green - from_green)/steps
	blue_step = float(to_blue - from_blue)/steps
	channel = str(channel)
	chred = eval('ch' + channel + 'r')
	chgreen = eval('ch' + channel + 'g')
	chblue = eval('ch' + channel + 'b')
	for step in range(0, steps+1):
        	red_value = int(from_red + red_step*step)
        	green_value = int(from_green + green_step*step)
        	blue_value = int(from_blue + blue_step*step)
        	pwm.setPWM(chred, 0, red_value)
        	pwm.setPWM(chgreen, 0, green_value)
        	pwm.setPWM(chblue, 0, blue_value)
		time.sleep(delay)

#fadefromto( 3, 0, 0, 0, 4000, 4000, 4000, 20, 0.1 )

#Path to Scenefile
scenepath = 'scenes-' + scenetype + '/' + scenefile + '.scn'

#read Scene-File into array
array = open(scenepath).read().split('\n')

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
setchannel(ch1r, val1r)
setchannel(ch1g, val1g)
setchannel(ch1b, val1b)
setchannel(ch2r, val2r)
setchannel(ch2g, val2g)
setchannel(ch2b, val2b)
setchannel(ch3r, val3r)
setchannel(ch3g, val3g)
setchannel(ch3b, val3b)
setchannel(ch4r, val4r)
setchannel(ch4g, val4g)
setchannel(ch4b, val4b)
setchannel(ch5r, val5r)
setchannel(ch5g, val5g)
setchannel(ch5b, val5b)


#time.sleep(3)

raw_input("wait")

i = 0
while i <= 14:
	pwm.setPWM(i, 0, 0)
	i = i + 1

#print sys.argv[1]
