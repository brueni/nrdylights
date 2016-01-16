#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time, sys

pwm = PWM(0x40)

pwm.setPWMFreq(80)

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
ch42 = 9
ch43 = 11
ch51 = 13
ch52 = 14
ch53 = 12

#Read Action-File
def readaction():
        actionfile = 'actions/next.action'
        array = open(actionfile).read().split('\n')
        action1 = str(array[0]) #Defines Type (static, dynamic)
        action2 = str(array[1]) #Defines Scene
	globals().update(locals())

#Read statefiles
def readcurrent():
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
	from42 = int(open('state/9.state').read())
	from43 = int(open('state/11.state').read())
	from51 = int(open('state/13.state').read())
	from52 = int(open('state/14.state').read())
	from53 = int(open('state/12.state').read())
	globals().update(locals())

#Write Channel Function
def setchannel( channel, valuepercent ):
	maxpercent = 4095
	value = valuepercent * maxpercent / 100
	pwm.setPWM(channel, 0, value)
	statefile = 'state/' + str(channel) + '.state'
	filehandle = open(statefile, "w")
	current_value = str(valuepercent)
	filehandle.write(current_value)
	filehandle.close()

#Read Desired Scene
def readscene( mode ):
	if mode == 'file':
		scenetype = action1
		scenefile = action2
		scenepath = 'scenes-' + scenetype + '/' + scenefile + '.scn'
	elif mode == 'exit':
		scenepath = 'scenes-static/all-off.scn'
	array = open(scenepath).read().split('\n')
	if array[0] == 'color':
		colorfile1 = 'color/' + array[1] + '.color'
		colorfile2 = 'color/' + array[2] + '.color'
		colorfile3 = 'color/' + array[3] + '.color'
		colorfile4 = 'color/' + array[4] + '.color'
		colorfile5 = 'color/' + array[5] + '.color'
		colorarray1 = open(colorfile1).read().split('\n')
		colorarray2 = open(colorfile2).read().split('\n')
		colorarray3 = open(colorfile3).read().split('\n')
		colorarray4 = open(colorfile4).read().split('\n')
		colorarray5 = open(colorfile5).read().split('\n')
		val11 = int(colorarray1[0])
		val12 = int(colorarray1[1])
		val13 = int(colorarray1[2])
		val21 = int(colorarray2[0])
		val22 = int(colorarray2[1])
		val23 = int(colorarray2[2])
		val31 = int(colorarray3[0])
		val32 = int(colorarray3[1])
		val33 = int(colorarray3[2])
		val41 = int(colorarray4[0])
		val42 = int(colorarray4[1])
		val43 = int(colorarray4[2])
		val51 = int(colorarray5[0])
		val52 = int(colorarray5[1])
		val53 = int(colorarray5[2])
	else:
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
	globals().update(locals())

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

def fadetoscene( steps, delay ):
        ch11_step = float(val11 - from11)/steps
        ch12_step = float(val12 - from12)/steps
        ch13_step = float(val13 - from13)/steps
        ch21_step = float(val21 - from21)/steps
        ch22_step = float(val22 - from22)/steps
        ch23_step = float(val23 - from23)/steps
        ch31_step = float(val31 - from31)/steps
        ch32_step = float(val32 - from32)/steps
        ch33_step = float(val33 - from33)/steps
        ch41_step = float(val41 - from41)/steps
        ch42_step = float(val42 - from42)/steps
        ch43_step = float(val43 - from43)/steps
        ch51_step = float(val51 - from51)/steps
        ch52_step = float(val52 - from52)/steps
        ch53_step = float(val53 - from53)/steps
        for step in range(0, steps+1):
                ch11_nextval = int(from11 + ch11_step*step)
                ch12_nextval = int(from12 + ch12_step*step)
                ch13_nextval = int(from13 + ch13_step*step)
                ch21_nextval = int(from21 + ch21_step*step)
                ch22_nextval = int(from22 + ch22_step*step)
                ch23_nextval = int(from23 + ch23_step*step)
                ch31_nextval = int(from31 + ch31_step*step)
                ch32_nextval = int(from32 + ch32_step*step)
                ch33_nextval = int(from33 + ch33_step*step)
                ch41_nextval = int(from41 + ch41_step*step)
                ch42_nextval = int(from42 + ch42_step*step)
                ch43_nextval = int(from43 + ch43_step*step)
                ch51_nextval = int(from51 + ch51_step*step)
                ch52_nextval = int(from52 + ch52_step*step)
                ch53_nextval = int(from53 + ch53_step*step)
                setchannel(ch11, ch11_nextval)
                setchannel(ch12, ch12_nextval)
                setchannel(ch13, ch13_nextval)
                setchannel(ch21, ch21_nextval)
                setchannel(ch22, ch22_nextval)
                setchannel(ch23, ch23_nextval)
                setchannel(ch31, ch31_nextval)
                setchannel(ch32, ch32_nextval)
                setchannel(ch33, ch33_nextval)
                setchannel(ch41, ch41_nextval)
                setchannel(ch42, ch42_nextval)
                setchannel(ch43, ch43_nextval)
                setchannel(ch51, ch51_nextval)
                setchannel(ch52, ch52_nextval)
                setchannel(ch53, ch53_nextval)
                time.sleep(delay)

#Read action-File every x seconds. If new action, execute.
readaction()
currentaction1 = ''
currentaction2 = ''
while action1 != 'exit':
	readaction()
        if action1 == 'exit':
                print 'Found Exit-Action, all Lights off...'
		readcurrent()
		readscene( 'exit' )
                fadetoscene( 5, 0.2)
                break
	if action1 != currentaction1 or action2 != currentaction2:
		readcurrent()
		readscene( 'file' )
		fadetoscene( 5, 0.2 )
	time.sleep(2)
	currentaction1 = action1
	currentaction2 = action2
		


#time.sleep(3)

#raw_input("wait")

#i = 0
#while i <= 14:
#	pwm.setPWM(i, 0, 0)
#	i = i + 1

#print sys.argv[1]
