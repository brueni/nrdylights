#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time, sys

pwm = PWM(0x40)

pwm.setPWMFreq(120)

def fadetoscene( scene, steps, delay ):
	ch = 1
	colorch = 1
	while ch <= 5:
		str_ch = str(ch)
		str_colorch = str(colorch)
		fromvar = 'from' + str_ch + str_colorch
		tovar = 'ch' + str_ch + str_colorch
		stepsize = float(tovar - fromvar)/steps		
		for step in range(0, steps+1):
		#schlaufe pro ch hier
	                red_value = int(from_red + red_step*step)
                	setchannel(chred, red_value)
                	time.sleep(delay)
		if colorch != 3:
			colorch = colorch + 1
		else:
			ch = ch + 1
			colorch = 1

fadetoscene( "x", "y", "z" )
