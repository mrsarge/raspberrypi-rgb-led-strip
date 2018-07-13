#!/usr/bin/env python

import cgi
import os

print "Content-type: text/html\n\n"

#Stop all currently running programms
reset = "pkill -9 -f LED.py"
os.system(reset)

form = cgi.FieldStorage()
action = form.getvalue('action')

if form.getvalue('speed'):
	speed = form.getvalue('speed')
	speed = str(round(int(speed) / 100.0,1))
else:
	speed = "0.0"
if form.getvalue('step'):
	step = form.getvalue('step')
else:
	step = "1"
if form.getvalue('delay'):
	delay = form.getvalue('delay')
	delay = str(round(int(delay) / 100.0,1))
else:
	delay = "0.0"
if form.getvalue('reverse'):
	reverse = form.getvalue('reverse')
else:
	reverse = "0"

if form.getvalue('color1'):
	color1 = form.getvalue('color1')
else:
	color1 = "ff0000"
if form.getvalue('color2'):
	color2 = form.getvalue('color2')
else:
	color2 = "ff00ff"
if form.getvalue('color3'):
	color3 = form.getvalue('color3')
else:
	color3 = "0000ff"
if form.getvalue('color4'):
	color4 = form.getvalue('color4')
else:
	color4 = "00ffff"
if form.getvalue('color5'):
	color5 = form.getvalue('color5')
else:
	color5 = "00ff00"
if form.getvalue('color6'):
	color6 = form.getvalue('color6')
else:
	color6 = "fff000"


cmd = "python LED.py " + action + " " + speed + " " + step + " " + delay + " " + reverse + " " + color1 + " " + color2 + " " + color3 + " " + color4 + " " + color5 + " " + color6 + "< /dev/null > /dev/null 2>&1 &"
os.system(cmd)

if action == "multi_color_fading":
	actionname = "Multi Color Fading"
elif action == "one_color":
	actionname = "One Color"
elif action == "two_color":
	actionname = "Two Color"
elif action == "three_color":
	actionname = "Three Color"
elif action == "four_color":
	actionname = "Four Color"
elif action == "five_color":
	actionname = "Five Color"
elif action == "six_color":
	actionname = "Six Color"
elif action == "all_color":
	actionname = "All Color"
else:
	actionname = "Stop"

speed = str(int(float(speed) * 100))
delay = str(int(float(delay) * 100))

print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">"
print "<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\">"
print "<head>"
print "<link rel=\"stylesheet\" href=\"../style.css\" type=\"text/css\" />"
print "<title>Status</title>"
print "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, user-scalable=false;\">"
print "</head>"
print "<body>"
print "</body>"
print "<table"
print "<tr>"
print "<td><p class=\"Title\">Status: " + actionname + ", done</td>"
print "</tr>"
print "<tr>"
if (actionname != "Stop"):
	print "<td><a class=\"Button\" href=\"../" + action + ".php?action=" + action + "&speed=" + speed + "&step=" + step + "&delay=" + delay + "&reverse=" + reverse + "&color1=" + color1 + "&color2=" + color2+ "&color3=" + color3+ "&color4=" + color4+ "&color5=" + color5+ "&color6=" + color6+ "\">Go Back</a></td>"
print "</tr>"
print "<tr>"
print "<td><a class=\"Button\" href=\"../index.php?" + action + ".php?action=" + action + "&speed=" + speed + "&step=" + step + "&delay=" + delay + "&reverse=" + reverse + "&color1=" + color1 + "&color2=" + color2+ "&color3=" + color3+ "&color4=" + color4+ "&color5=" + color5+ "&color6=" + color6+ "\">Main Menu</a></td>"
print "</tr>"
print "<tr>"
if (actionname != "Stop"):
	print "<td><a class=\"Button\" href=\"command.py?action=stop&&speed=" + speed + "&step=" + step + "&delay=" + delay + "&reverse=" + reverse + "&color1=" + color1 + "&color2=" + color2+ "&color3=" + color3+ "&color4=" + color4+ "&color5=" + color5+ "&color6=" + color6+ "\">Turn Off</a></td>"
print "</tr>"
print "</table"
print "</body>"
print "</html>"