## qRobot Command Line Interface toolkit, Simple Python Scripts


This is repo for one day project to create "Simple python scripts to manipulate 
cheap 6 DOF Robot Arm kit  using Adafruit 16 Channel PWM/Servo driver board 
with Raspberry Pi 3 Model B board. I just implement simple command line interface 
for tuning and understanding of basic moves required for 6 DOF Robot Arm Kit.

Here are the ingredients of simple but cheap 6 DOF Robot Arm Kits
* 6 DOF Robo Arm Kits, bolt and nuts and frame you can buy from ebay.com
* 6 servo motors which you can also buy from either ebay.com or amazon.com
* Adafruit 16 Channel PWM/Servo Driver board
* Raspberry Pi 3 Model B (Rasbian Jessie May 2016, Kernel version 4.4)
  - Enabled I2C (You can find good tutorial how to at many differnt website and 
   (https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)
* And delightful mind to work on

Scripts are small and very simple because I just implemented in couple of hours
while I am testing/tuning the moving ment. To use these small scripts, you need to
download Adafruit-PWM-Servo-Driver-Library at 

https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library

Here are simple but useful comment sets.

## align joint at 90 Degree
">>" align <ch> 
  <ch> : 0 ~ 5 for 6DOF

## align all joints at 90 Degree
">>" alignall 

## move the servo to the specific degree
">>" move <ch> <angle>
  <ch> : 0 ~ 5 for 6 DOF
  <angle> : 0 ~ 180 Degree
  
## go to the sleep position
">>" sleep

## go to ready-for-the-work position
">>" ready

## print currnent angle position for all joints
">>" status
{0:90, 1:20, 2:30, 3:50, 4:60, 5: 50}

## wakeup from the sleep poistion and go to the ready position
">>" wake

These scripts are not final sets at all because I just wanted to have basic interactive 
tools for tuning/testing the move. And did not used any parsing aids (lex/yacc/bison/...)
to make my code simple.  You probably understand the code in 10 minutes to add or remove 
comments. To me this small set of scripts are useful to move forward. I can't promise anything,
but I will update if there is any update. But for now, this is more than
enough for me to move on to the next step, "working with ROS and matlab robotics toolbox".

Thanks,

pksuf07
