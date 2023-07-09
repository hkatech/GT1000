#!/bin/bash
echo "<< Bank 0 >>"
echo "============"
echo "0x38: " $(./b21.sh ; sleep 1 ; sudo i2cget -y 1 0x38)
echo "0x39: " $(sudo i2cget -y 1 0x39)
echo "0x3a: " $(sudo i2cget -y 1 0x3a)
echo "0x3b: " $(sudo i2cget -y 1 0x3b)
echo "0x3c (- - AFB2.2/4/5/7/8  -): " $(sudo i2cget -y 1 0x3c)
echo "0x3d (LED_R.1/2/3 -  - - - -): " $(sudo i2cget -y 1 0x3d)
echo "0x3e: " $(sudo i2cget -y 1 0x3e)
echo "0x3f: " $(sudo i2cget -y 1 0x3f)
## For bank 1 use b20.sh
echo "<< Bank 1 >>"
echo "============"
echo "0x38: " $(./b20.sh ; sleep 1 ; sudo i2cget -y 1 0x38)
echo "0x39: " $(sudo i2cget -y 1 0x39)
echo "0x3a (LED_L.1/2/3 WIPER.1/2/3/4 -): " $(sudo i2cget -y 1 0x3a)
echo "0x3b: " $(sudo i2cget -y 1 0x3b)
echo "0x3c: " $(sudo i2cget -y 1 0x3c)
echo "0x3d (- - -  - POST- - -): " $(sudo i2cget -y 1 0x3d)
echo "0x3e: " $(sudo i2cget -y 1 0x3e)
echo "0x3f (WASHER.1/2 - -  - - - -): " $(sudo i2cget -y 1 0x3f)
## For bank 2 use b16.sh
echo "<< Bank 2 >>"
echo "============"
echo "0x38: " $(./b16.sh ; sleep 1 ; sudo i2cget -y 1 0x38)
echo "0x39: " $(sudo i2cget -y 1 0x39)
echo "0x3a: " $(sudo i2cget -y 1 0x3a)
echo "0x3b: " $(sudo i2cget -y 1 0x3b)
echo "0x3c (AFB2.1/3/6 -  - - - -): " $(sudo i2cget -y 1 0x3c)
echo "0x3d (ACC POST+ - -  - - - -): " $(sudo i2cget -y 1 0x3d)
echo "0x3e: Not Installed"
echo "0x3f: Not Installed"
#echo "0x3e: " $(sudo i2cget -y 1 0x3e)
#echo "0x3f: " $(sudo i2cget -y 1 0x3f)
