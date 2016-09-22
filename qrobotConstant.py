#!/usr/bin/python

#-- qrobotConstant.py
import sys

#-- exit
#-- quit
#-- alignall
#-- move 1 90
#-- align 1  
#-- define commands

CMD_EXIT=0
CMD_QUIT=1
CMD_ALIGN=2
CMD_ALIGNALL=3
CMD_MOVE=4
CMD_GRAB=5
CMD_STATUS=6
CMD_SLEEP=7
CMD_WAKEUP=8
CMD_READY=9
CMD_DONOTHING=10

channels=[0,1,2,3,4,5]	#-- 6 DOF

#-- command dictionary
cmds =	{ 			
	'exit' : CMD_EXIT,
	'quit' : CMD_QUIT,
	'align': CMD_ALIGN,
	'alignall': CMD_ALIGNALL,
	'move': CMD_MOVE,
	'grab': CMD_GRAB,
	'status': CMD_STATUS,
	'sleep': CMD_SLEEP,
	'wakeup': CMD_WAKEUP,
	'ready': CMD_READY,
	''	: CMD_DONOTHING
	}

#-- for Adafruit_PWM_Servo_Driver
servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
delta=(servoMax-servoMin)
oneDeg=float(delta/180.0)
