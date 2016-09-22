#!/usr/bin/python

import sys
from qrobotConstant import *

def qrobotProcessor(istrs):
	cmd=-1
	charg=-1
	angle=0
	error_code=0

	cmdstrset=istrs.split(" ")	
	print(cmdstrset)
	if len(cmdstrset) == 0 : 
		print("do nothing") 
	passcnt=1
	for token in cmdstrset: 
		#-- first pass --------------------------------
		if passcnt==1 and token in cmds:
			cmd = cmds[token]
			print ("cmd : %s(%d)" % (token, cmd))
			if cmd == CMD_EXIT or cmd == CMD_QUIT :
				error_code=0
				break		#-- end of exit/quit

			if cmd == CMD_ALIGN :
				pass		#-- move to next pass

			if cmd == CMD_ALIGNALL :
				error_code=0
				break		#-- end of alignall
		
			if cmd == CMD_MOVE:
				pass		#-- move to next pass

			if cmd == CMD_GRAB:
				error_code=0	#-- move to next pass
				pass
			if cmd == CMD_SLEEP:	
				error_code=0
				break		# end of sleep
		
			if cmd == CMD_STATUS:
				error_code=0
				break		# end of status
		
			if cmd == CMD_WAKEUP:
				error_code=0
				break		# end of wakeup

			if cmd == CMD_READY:
				error_code=0
				break;		# end of ready

		elif passcnt==1 and token not in cmds:
			print("command syntax error: worng command")
			error_code=-1;
			break			#-- cmd syntax error

		#-- second pass --------------------------------	
		if passcnt==2 :
			charg=int(token)
			print("charg : %d" % (charg))
			if cmd == CMD_ALIGN or cmd == CMD_MOVE : #-- align
				if charg in channels:
					if cmd == CMD_ALIGN:
						error_code=0
						break	#-- end of align cmd	
					if cmd == CMD_MOVE:
						pass	#-- move to 3rd pass	
				else:
					print("command syntax error: wrong channel number")
					error_code=-1
					break	#-- cmd syntax error

			if cmd == CMD_GRAB:	#-- grab
				#-- charg is actual speed of grabbing from 0 to 5
				charg = charg % 3 + 1
				error_code=0
				break;

		#-- third pass ----------------------------------	
		if passcnt==3 :
			angle=int(token)
			if angle > 180:
				angle=angle % 180	#-- module of 180
			print("angle : %d" % (angle))
			if cmd == CMD_MOVE:
				error_code=0
				break		#-- end of move cmd
			else: 
				print("command syntax error: wrong angle")
				error_code=-1
				break		#-- cmd syntax error
		passcnt +=1

	return cmd, charg, angle, error_code
		

def main():
	while True:
		istrs=raw_input(">> ")
		cmd, charg, angle, error_code = qrobotProcessor(istrs)
		print("%d, %d, %d, %d" % (cmd, charg, angle, error_code))
		if cmd == 0 or cmd  == 1 :
			sys.exit(0)

if __name__ == "__main__":
	main()
