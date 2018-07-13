#!/usr/bin/env python

import os

stopb = "echo 4=0 > /dev/pi-blaster"
stopr = "echo 17=0 > /dev/pi-blaster"
stopg = "echo 18=0 > /dev/pi-blaster"

os.system(stopb)
os.system(stopr)
os.system(stopg)