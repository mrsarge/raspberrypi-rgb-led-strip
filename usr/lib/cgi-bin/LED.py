#!/usr/bin/env python

import sys
import time
import os
import operator

#define GPIO pin number
pinRed = "4"
pinGreen = "17"
pinBlue = "18"

# Define List and List Lists
colorList = [[] for _ in range(7)]
colorOps = []
colorOpsReverse = []
colorStep = []
execColor = []
colorDone = []

# Assign variable from command line or stop everything
if len(sys.argv) == 12:
	ACTION = sys.argv[1]
	SPEED = float(sys.argv[2])
	STEP = int(sys.argv[3])
	DELAY = float(sys.argv[4])
	REVERSE = int(sys.argv[5])
	COLOR = {}
	for i in range(1, 7):
		COLOR[i] = sys.argv[i + 5]

else:
	ACTION = "stop"
	SPEED = "0"
	STEP = "1"
	DELAY = "0"
	COLOR = {}
	for i in range(1, 7):
		COLOR[i] = "000000"

# Define Command to run	
def pwm(pin, power):
	if pin == 0:
		pin = pinRed
	elif pin == 1:
		pin = pinGreen
	elif pin == 2:
		pin = pinBlue
	power = power / 100.0
	#print "servo[" + str(pin) + "][" + str(power) + "]"
	cmd = "echo " + str(pin) + "=" + str(power) + " > /dev/pi-blaster"
	os.system(cmd)

# Define Convert to Int function
convertInt = lambda x: int(x) if isinstance(x, int) else x

# Define operator
ops = {
"<=": operator.le,
">=": operator.ge,
"==": operator.eq
}

# Define HEX to Percent formula
def hex2per(colNumber, color):
	if color == 1:
		return int(round(float(int(colNumber[:-4], 16) / 255.0 * 100), 2));
	elif color == 2:
		return int(round(float(int(colNumber[-4:-2], 16) / 255.0 * 100), 2));
	elif color == 3:
		return int(round(float(int(colNumber[-2:], 16) / 255.0 * 100), 2));

# Get Color Percent value and store in colorList
for i in range(1, 7):
	for j in range(0, 3):
		colorList[i].append(hex2per(COLOR[i], j + 1))

# Define operator and step assignment
def opsStep(color1, color2, index):
	if (color1 > color2):
		colorStep.append(-STEP)
		colorOps.append(">=")
		colorOpsReverse.append("<=")
	elif (color1 < color2):
		colorStep.append(STEP)
		colorOps.append("<=")
		colorOpsReverse.append(">=")
	else:
		colorStep.append(1)
		colorOps.append("==")
		colorOpsReverse.append("==")
		
# Define Color Fade function
def colorFade(color1, color2):
	for i in range(0, 3):
		# Evaluate if Color1 is greater than Color2
		opsStep(colorList[color1][i], colorList[color2][i], 1)
		# Prepare execColor variable that are sent to pi-blaster
		execColor.append(colorList[color1][i])
		# Initialise colorDone variable to know when a color fade is over
		colorDone.append(False)
	while True:
			# Step each color by one step. switch colorDone to True when
			# execColor[i] as reached color[2][i]
			for i in range(0, 3):
				if ops[colorOps[i]](execColor[i] + colorStep[i], colorList[color2][i]):
					execColor[i] = execColor[i] + colorStep[i]
				else:
					colorDone[i] = True
			# If the 3 fade are finish, set execColor[1] to colorList[2]
			# and sent to pi-blaster
			if (colorDone[0] == colorDone[1] == colorDone[2] == True):
				for i in range(0, 3):
					execColor[i] = colorList[color2][i]
					pwm(i,execColor[i])
				print "rouge: ",execColor[0]," vert: ",execColor[1]," bleu: ",execColor[2]
				# Wait for a Delay before starting the next color fade
				# if user wanted it
				time.sleep(DELAY)
				# reset colorDone variable
				del colorDone[:]
				del colorStep[:]
				del colorOps[:]
				del colorOpsReverse[:]
				# break to start the next fade
				
				break
			# If the 3 fade are not finished, send current level to pi-blaster
			for i in range(0, 3):
				pwm(i,execColor[i])
			print "rouge: ",execColor[0]," vert: ",execColor[1]," bleu: ",execColor[2]
			# wait for a delay to slow down the loop if user wanted it
			time.sleep(SPEED)
			



if ACTION =="one_color":
	for i in range(0, 3):
		pwm(i, colorList[1][i])
			
elif ACTION == "two_color":

	while True:
		colorFade(1, 2)
		colorFade(2, 1)						

elif ACTION == "three_color":

	while True:
		colorFade(1, 2)
		colorFade(2, 3)
		if REVERSE == True:
			colorFade(3,2)
			colorFade(2,1)
		else:
			colorFade(3, 1)

elif ACTION == "four_color":

	while True:
		colorFade(1, 2)
		colorFade(2, 3)
		colorFade(3, 4)
		if REVERSE == True:
			colorFade(4,3)
			colorFade(3,2)
			colorFade(2,1)
		else:
			colorFade(4, 1)

elif ACTION == "five_color":

	while True:
		colorFade(1, 2)
		colorFade(2, 3)
		colorFade(3, 4)
		colorFade(4, 5)
		if REVERSE == True:
			colorFade(5,4)
			colorFade(4,3)
			colorFade(3,2)
			colorFade(2,1)
		else:
			colorFade(5, 1)

elif ACTION == "six_color":

	while True:
		colorFade(1, 2)
		colorFade(2, 3)
		colorFade(3, 4)
		colorFade(4, 5)
		colorFade(5, 6)
		if REVERSE == True:
			colorFade(6,5)
			colorFade(5,4)
			colorFade(4,3)
			colorFade(3,2)
			colorFade(2,1)
		else:
			colorFade(6, 1)

elif ACTION == "all_color":
	pwm(0,100)
	while True:
		time.sleep(DELAY)
		for i in range(0, 100, STEP):
			if (i + STEP <= 100):
				pwm(1,i)
				time.sleep(SPEED)
			else:
				pwm(1,100)
				time.sleep(SPEED)
				break
		time.sleep(DELAY)
		for i in range(100, 0, -STEP):
			if (i + STEP >= 0):
				pwm(0,i)
				time.sleep(SPEED)
			else:
				pwm(1,0)
				time.sleep(SPEED)
				break
		time.sleep(DELAY)
		for i in range(0, 100, STEP):
			if (i + STEP <= 100):
				pwm(2,i)
				time.sleep(SPEED)
			else:
				pwm(2,100)
				time.sleep(SPEED)
				break
		time.sleep(DELAY)
		for i in range(100, 0, -STEP):
			if (i + STEP >= 0):
				pwm(1,i)
				time.sleep(SPEED)
			else:
				pwm(1,0)
				time.sleep(SPEED)
				break
		time.sleep(DELAY)
		for i in range(0, 100, STEP):
			if (i + STEP <= 100):
				pwm(0,i)
				time.sleep(SPEED)
			else:
				pwm(0,100)
				time.sleep(SPEED)
				break
		time.sleep(DELAY)
		for i in range(100, 0, -STEP):
			if (i + STEP >= 0):
				pwm(2,i)
				time.sleep(SPEED)
			else:
				pwm(2,0)
				time.sleep(SPEED)
				break


		
	
else:
	stopb = "echo 4=0 > /dev/pi-blaster"
	stopr = "echo 17=0 > /dev/pi-blaster"
	stopg = "echo 18=0 > /dev/pi-blaster"

	os.system(stopb)
	os.system(stopr)
	os.system(stopg)

	sys.exit()


