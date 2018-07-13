# raspberrypi-rgb-led-strip

Follow this tutorials for LED wiring : http://mitchtech.net/raspberry-pi-pwm-rgb-led-strip/

If not already done, install apache2 and php5:  
```sudo apt-get install apache2 php5```

Enable CGI support in apache:  
```sudo a2enmod cgid```

Restart apache:  
```sudo /etc/init.d/apache2 restart```

Copy all files from this repo to the Pi in the right folder  

Make sure the python files in the cgi-bin folder have the executable flag:  
```sudo chmod +x *.py```

Set the pin number you use in the \usr\lib\cgi-bin\LED.py file.  Default are 4, 17 and 18.

Install autoconf:  
```sudo apt-et install autoconf```

Install pi-blaster from : https://github.com/sarfata/pi-blaster/ :  
```
git clone https://github.com/sarfata/pi-blaster.git
cd pi-blaster
./autogen.sh
./configure
make
sudo make install
```

Enable pi-blaster and autostart:  
```sudo systemctl enable pi-blaster.service```


Open a browser on http://Raspberrypi_Ip_Address

Enjoy!
