<?php
define('action', '');
define('speed', '');
define('step', '');
define('delay', '');
define('reverse', '');
define('color1', '');
define('color2', '');
define('color3', '');
define('color4', '');
define('color5', '');
define('color6', '');
if (isset($_GET['action'])){
	$action = $_GET['action'];
} else {
	$action = '';
}
if(isset($_GET['speed'])){
	$speed = $_GET['speed'];
} else {
	$speed = '0';
}
if(isset($_GET['step'])){
	$step = $_GET['step'];
} else {
	$step = '1';
}
if(isset($_GET['delay'])){
	$delay = $_GET['delay'];
} else {
	$delay = '0';
}
if(isset($_GET['reverse'])){
	$reverse = $_GET['reverse'];
} else {
	$reverse = '0';
}
if(isset($_GET['color1'])){
	$color1 = $_GET['color1'];
}
if(isset($_GET['color2'])){
	$color2 = $_GET['color2'];
}
if(isset($_GET['color3'])){
	$color3 = $_GET['color3'];
}
if(isset($_GET['color4'])){
	$color4 = $_GET['color4'];
}
if(isset($_GET['color5'])){
	$color5 = $_GET['color5'];
}
if(isset($_GET['color6'])){
	$color6 = $_GET['color6'];
}
if ($color1 == "" || hexdec($color1) > 16777215) {$color1 = "ff0000";}
if ($color2 == "" || hexdec($color2) > 16777215) {$color2 = "ff00ff";}
if ($color3 == "" || hexdec($color3) > 16777215) {$color3 = "0000ff";}
if ($color4 == "" || hexdec($color4) > 16777215) {$color4 = "00ffff";}
if ($color5 == "" || hexdec($color5) > 16777215) {$color5 = "00ff00";}
if ($color6 == "" || hexdec($color6) > 16777215) {$color6 = "fff000";}
?>


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<link rel="stylesheet" href="style.css" type="text/css" />
    <title>Two Color</title>
    <script type="text/javascript" src="jscolor/jscolor.js"></script>
	<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=false;">
</head>
<body>
<FORM name="two_color" action="/cgi-bin/command.py" method="GET">
	<p><input type="text" name="action" value="two_color" style="display: none;"></p>
		<table>
			<tr>
				<td colspan="3"><p class="Title">Two color</p></td>
			</tr>
			<tr>
				<td colspan="3"><p><a  class="Button" href="index.php?action=<?php echo $action ?>&speed=<?php echo $speed ?>&step=<?php echo $step ?>&delay=<?php echo $delay ?>&reverse=<?php echo $reverse ?>&color1=<?php echo $color1 ?>&color2=<?php echo $color2 ?>&color3=<?php echo $color3 ?>&color4=<?php echo $color4 ?>&color5=<?php echo $color5 ?>&color6=<?php echo $color6 ?>">Main Menu</a></p></td>
			</tr>
			<tr>
				<td colspan="3"><p><input class="color" type="text" name="color1" id="color1" maxlength="6" size="20px" value="<?php echo $color1 ?>"></p></td>
			</tr>
			<tr>
				<td colspan="3"><p><input class="color" type="text" name="color2" id="color2" maxlength="6" value="<?php echo $color2 ?>"></p></td>
			</tr>				
			<tr>
				<td class="tdLeft">Speed:</td>
				<td><input class="Range" type="range" min="0" max="100" step="1" name="speed" value="<?php echo $speed ?>" onchange="showValueSpeed(this.value)"/></td>
				<td class="tdRight"><span id="speedRange"><?php echo $speed ?></span></td>
				<script type="text/javascript">
					function showValueSpeed(newValue)
					{
						document.getElementById("speedRange").innerHTML=newValue;
					}
				</script>
			</tr>
			<tr>
				<td class="tdLeft">Step:</td>
				<td><input class="Range" type="range" min="1" max="100" step="1" name="step" value="<?php echo $step ?>" onchange="showValueStep(this.value)"/></td>
				<td class="tdRight"><span id="stepRange"><?php echo $step ?></span></td>
				<script type="text/javascript">
					function showValueStep(newValue)
					{
						document.getElementById("stepRange").innerHTML=newValue;
					}
				</script>
			</tr>
			<tr>
				<td class="tdLeft">Delay:</td>
				<td><input class="Range" type="range" min="0" max="100" step="1" name="delay" value="<?php echo $delay ?>" onchange="showValueDelay(this.value)"/></td>
				<td class="tdRight"><span id="delayRange"><?php echo $delay ?></span></td>
				<script type="text/javascript">
					function showValueDelay(newValue)
					{
						document.getElementById("delayRange").innerHTML=newValue;
					}
				</script>
			</tr>
			<tr>
				<td class="tdLeft">Reverse:</td>
				<td>&nbsp;&nbsp;<input type="checkbox" name="Reverse" value="<? echo $reverse ?>"></td>
			</tr>
			<tr>
				<td colspan="3"><p><input type="submit" value="Activate" class="Button"></p></td>
			</tr>
			<tr>
				<td colspan="3"><br /><p><a  class="Button" href="two_color.php">Reset Color</a></p></td>
			</tr>
			<tr>
				<td colspan="3"><p><a  class="Button" href="/cgi-bin/command.py?action=stop&speed=<?php echo $speed ?>&step=<?php echo $step ?>&delay=<?php echo $delay ?>&reverse=<?php echo $reverse ?>&color1=<?php echo $color1 ?>&color2=<?php echo $color2 ?>&color3=<?php echo $color3 ?>&color4=<?php echo $color4 ?>&color5=<?php echo $color5 ?>&color6=<?php echo $color6 ?>">Turn Off</a></p></td>
			</tr>
		</TABLE>
	</FORM>
</body>
</html>
