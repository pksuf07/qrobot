#!/usr/bin/env python

import sys
import time
from qrobotConstant import *
from qrobotCmd import qrobotProcessor
from Adafruit_PWM_Servo_Driver import PWM

#-- current angle position of all joint
curAngles=dict()

def setServoPulse(pwm, channel, pulse):
	pulseLength = 1000000                   # 1,000,000 us per second
	pulseLength /= 60                       # 60 Hz
	print "%d us per period" % pulseLength
	pulseLength /= 4096                     # 12 bits of resolution
	print "%d us per bit" % pulseLength
	pulse *= 1000
	pulse /= pulseLength
	print "pulse = %d" % pulse
	pwm.setPWM(channel, 0, pulse)

def init():
	#-- initialization 
	pwm = PWM(0x40)
	pwm.setPWMFreq(60)                      # Set frequency to 60 Hz
	setServoPulse(pwm, 1, 100)		#
	print "delta=%d, oneDeg=%f" % (delta, oneDeg)
	for i in channels : curAngles[i]=0
	ready(pwm)
	return pwm

def ready(pwm):
	alignall(pwm)
	#-- channel 2
	for i in range(90, 181, 1):
		move(pwm, 2, i)
	curAngles[2]=180
	#-- channel 3
	for i in range(90, 121, 1):
		move(pwm, 3, i)	
	curAngles[3]=120

def wakeup(pwm):
	#-- assumed from sleep position [0:90, 1:0, 2:0, 3:0, 4:0, 5:0]
	#-- wake up from the sleep [0:90, 1:90: 3:90, 4:90, 5:90]
	newangle=90
	for ch in channels:
		curangle=curAngles[ch]
		if newangle < curangle :
			incr = -1
		else:
			incr=1
		for i in range (curangle, newangle, incr): #-- slow wake up
			move(pwm, ch, i)	

	for i in range(1, 5, 1):
		curAngles[i]=90

def move(pwm, ch, newangle):
	curangle=curAngles[ch]
	if curangle == newangle :
		return 0

	if newangle < curangle:
		incr=-1
	else:
		incr=1

	for ang in range (curangle, newangle, incr):
		to = float(servoMin+ang*oneDeg)
		pwm.setPWM(ch, 0, int(to) )
		
	curAngles[ch]=newangle
	return 0

def status():
	print(curAngles)

def sleep(pwm):
	move(pwm, 0, 180)
	#-- go to sleep position
	move(pwm, 3, 0)
	time.sleep(0.5)
	move(pwm, 2, 0)
	time.sleep(0.5)
	#-- need to go slow for ch 1
	curangle=curAngles[1]	
	for an in (curangle, 0, -1): move(pwm, 1, an) 
	time.sleep(0.5)
	move(pwm, 0, 90)
	time.sleep(0.5)
	print("sleep position: [0:90, 1:0, 2:0, 3:0, 4:0, 5:0]")


def grab(pwd, speed):
	#-- the speed of grab: 1 ~ 3
	#-- make it wide and grab
	gspeed=speed*10
	for ang in range (0, 180, gspeed):	
		move(pwm, 5, ang)	#-- only for channel 5 (hand)

def align(pwm, channel):
	move(pwm, channel, 90)
	curAngles[channel]=90

def alignall(pwm):
	#-- for all channels
	time.sleep(0.2)
	for ch in channels:
		move(pwm, ch, 90)
		time.sleep(0.2)

def qrobotCLIprocessor(pwm, cmd, ch, angle, error_code):
	if cmd == CMD_EXIT or cmd == CMD_QUIT : 
		print("Bye")
		sys.exit(0)
	elif cmd == CMD_ALIGNALL:
		alignall(pwm)
	elif cmd == CMD_ALIGN:
		align(pwm, ch)
	elif cmd == CMD_MOVE:
		move(pwm, ch, angle)
	elif cmd == CMD_SLEEP:
		sleep(pwm)
	elif cmd == CMD_STATUS:
		status()
	elif cmd == CMD_WAKEUP:
		wakeup(pwm)
	elif cmd == CMD_READY:
		ready(pwm)
	else:
		print("unknown error")	

def qrobotCLI(pwm):
	cmd=0
	ch=0
	angle=0
	error_code=0

	while True:
		istrs=raw_input(">> ")
		cmd, ch, angle, error_code=qrobotProcessor(istrs)
		qrobotCLIprocessor(pwm, cmd, ch, angle, error_code)

#-- 6-DOF, channels=[0,1,2,3,4,5], at max

def main(pwm, channels):
	qrobotCLI()	

if __name__ == "__main__":
	pwm=init()
	qrobotCLI(pwm)
