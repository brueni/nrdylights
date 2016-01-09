#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time, sys

pwm = PWM(0x40)

pwm.setPWMFreq(120)

#define Channels, 1=red, 2=green, 3=blue, and so on
ch11 = 1
ch12 = 2
ch13 = 0
ch21 = 4
ch22 = 3
ch23 = 8
ch31 = 5
ch32 = 7
ch33 = 6
ch41 = 10
ch42 = 11
ch43 = 9
ch51 = 13
ch52 = 12
ch53 = 14

#Arg1 - Static or Dynamic
scenetype = sys.argv[1]

#Arg2 - Scenefile
scenefile = sys.argv[2]

#Path to Scenefile
scenepath = 'scenes-' + scenetype + '/' + scenefile + '.scn'

#Read statefiles
from11 = int(open('state/1.state').read())
from12 = int(open('state/2.state').read())
from13 = int(open('state/0.state').read())
from21 = int(open('state/4.state').read())
from22 = int(open('state/3.state').read())
from23 = int(open('state/8.state').read())
from31 = int(open('state/5.state').read())
from32 = int(open('state/7.state').read())
from33 = int(open('state/6.state').read())
from41 = int(open('state/10.state').read())
from42 = int(open('state/11.state').read())
from43 = int(open('state/9.state').read())
from51 = int(open('state/13.state').read())
from52 = int(open('state/12.state').read())
from53 = int(open('state/14.state').read())

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
	chred = eval('ch' + channel + '1')
	chgreen = eval('ch' + channel + '2')
	chblue = eval('ch' + channel + '3')
	for step in range(0, steps+1):
        	red_value = int(from_red + red_step*step)
        	green_value = int(from_green + green_step*step)
        	blue_value = int(from_blue + blue_step*step)
        	setchannel(chred, red_value)
        	setchannel(chgreen, green_value)
        	setchannel(chblue, blue_value)
		time.sleep(delay)

def fadetoscene( scene, steps, delay ):
        ch = 1
        colorch = 1
	while ch <= 5:
		str_ch = str(ch)
        	str_colorch = str(colorch)
        	fromvar  = 'from' + str_ch + str_colorch
        	tovar = 'val' + str_ch + str_colorch
	#	stepsize = float(eval(tovar) - eval(fromvar))/steps  
		if colorch != 3:
                	colorch = colorch + 1
       		else:
                	ch = ch + 1
                	colorch = 1
	stepsize11 = float(val11 - from11)/steps
	stepsize12 = float(val12 - from12)/steps
	stepsize13 = float(val13 - from13)/steps
	stepsize21 = float(val21 - from21)/steps
	stepsize22 = float(val22 - from22)/steps
	stepsize23 = float(val23 - from23)/steps
	stepsize31 = float(val31 - from31)/steps
	stepsize32 = float(val32 - from32)/steps
	stepsize33 = float(val33 - from33)/steps
	stepsize41 = float(val41 - from41)/steps
	stepsize42 = float(val42 - from42)/steps
	stepsize43 = float(val43 - from43)/steps
	stepsize51 = float(val51 - from51)/steps
	stepsize52 = float(val52 - from52)/steps
	stepsize53 = float(val53 - from53)/steps
	for step in range(0, steps+1):
		setval11 = int(eval(fromvar) + stepsize11*step)
		setval12 = int(eval(fromvar) + stepsize12*step)
		setval13 = int(eval(fromvar) + stepsize13*step)
		setval21 = int(eval(fromvar) + stepsize21*step)
		setval22 = int(eval(fromvar) + stepsize22*step)
		setval23 = int(eval(fromvar) + stepsize23*step)
		setval31 = int(eval(fromvar) + stepsize31*step)
		setval32 = int(eval(fromvar) + stepsize32*step)
		setval33 = int(eval(fromvar) + stepsize33*step)
		setval41 = int(eval(fromvar) + stepsize41*step)
		setval42 = int(eval(fromvar) + stepsize42*step)
		setval43 = int(eval(fromvar) + stepsize43*step)
		setval51 = int(eval(fromvar) + stepsize51*step)
		setval52 = int(eval(fromvar) + stepsize52*step)
		setval53 = int(eval(fromvar) + stepsize53*step)
		setchannel(ch11, setval11)
		setchannel(ch12, setval12)
		setchannel(ch13, setval13)
		setchannel(ch21, setval21)
		setchannel(ch22, setval22)
		setchannel(ch23, setval23)
		setchannel(ch31, setval31)
		setchannel(ch32, setval32)
		setchannel(ch33, setval33)
		setchannel(ch41, setval41)
		setchannel(ch42, setval42)
		setchannel(ch43, setval43)
		setchannel(ch51, setval51)
		setchannel(ch52, setval52)
		setchannel(ch53, setval53)
		#ch = 1
		#colorch = 1
		#while ch <= 5:
		#	str_ch = str(ch)
                #	str_colorch = str(colorch)
		#	currentchannel = eval('ch' + str_ch + str_colorch)
		#	currentval = eval('setval' + str_ch + str_colorch)
		#setchannel(currentchannel, currentval)
		#	if colorch != 3:
		#		colorch = colorch + 1
		#	else:
		#		ch = ch + 1
		#		colorch = 1
		time.sleep(delay)

#fadefromto( 3, 4000, 4000, 4000, 0, 0, 0, 20, 0.1 )

#read Scene-File into array
array = open(scenepath).read().split('\n')

#put array-values into vars
val11 = int(array[0])
val12 = int(array[1])
val13 = int(array[2])
val21 = int(array[3])
val22 = int(array[4])
val23 = int(array[5])
val31 = int(array[6])
val32 = int(array[7])
val33 = int(array[8])
val41 = int(array[9])
val42 = int(array[10])
val43 = int(array[11])
val51 = int(array[12])
val52 = int(array[13])
val53 = int(array[14])

#set all channels to values
#setchannel(ch11, val11)
#setchannel(ch12, val12)
#setchannel(ch13, val13)
#setchannel(ch21, val21)
#setchannel(ch22, val22)
#setchannel(ch23, val23)
#setchannel(ch31, val31)
#setchannel(ch32, val32)
#setchannel(ch33, val33)
#setchannel(ch41, val41)
#setchannel(ch42, val42)
#setchannel(ch43, val43)
#setchannel(ch51, val51)
#setchannel(ch52, val52)
#setchannel(ch53, val53)

fadetoscene( scenepath, 10, 0.2 )

#time.sleep(3)

#raw_input("wait")

#i = 0
#while i <= 14:
#	pwm.setPWM(i, 0, 0)
#	i = i + 1

#print sys.argv[1]
