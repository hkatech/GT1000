#!/bin/bash
if [ $# -ne 3 ]
  then
    echo "Usage: portCheck ouputPort inputPort inputBank"
    exit
fi
echo "Output: " $1 " Input:" $2 " on bank " $3
echo "Testing : " $(echo "Test :" $1 " and " $2)
echo "0x01: " $(./b16.sh ; sudo i2cset -y 1 $1 0xfe) " " $(./b21.sh ; sleep 1 ; sudo i2cget -y 1 $2  ; ./b16.sh)
echo "0x02: " $(sudo i2cset -y 1 $1 0xfd) " " $(./b21.sh ; sleep 1 ; sudo i2cget -y 1 $2  ; ./b16.sh)
echo "0x04: " $(sudo i2cset -y 1 $1 0xfb) " " $(./b21.sh ; sleep 1 ; sudo i2cget -y 1 $2  ; ./b16.sh)
echo "0x08: " $(sudo i2cset -y 1 $1 0xf7) " " $(./b21.sh ; sleep 1 ; sudo i2cget -y 1 $2  ; ./b16.sh)
echo "0x10: " $(sudo i2cset -y 1 $1 0xef) " " $(./b21.sh ; sleep 1 ; sudo i2cget -y 1 $2  ; ./b16.sh)
echo "0x20: " $(sudo i2cset -y 1 $1 0xdf) " " $(./b21.sh ; sleep 1 ; sudo i2cget -y 1 $2  ; ./b16.sh)
echo "0x40: " $(sudo i2cset -y 1 $1 0xbf) " " $(./b21.sh ; sleep 1 ; sudo i2cget -y 1 $2  ; ./b16.sh)
echo "0x80: " $(sudo i2cset -y 1 $1 0x7f) " " $(./b21.sh ; sleep 1 ; sudo i2cget -y 1 $2  ; ./b16.sh)
#echo "0x38: " $(sudo i2cget -y 1 0x38)
#echo "0x39: " $(sudo i2cget -y 1 0x39)
#echo "0x3a: " $(sudo i2cget -y 1 0x3a)
#echo "0x3b: " $(sudo i2cget -y 1 0x3b)
#echo "0x3c: " $(sudo i2cget -y 1 0x3c)
#echo "0x3d: " $(sudo i2cget -y 1 0x3d)
#echo "0x3e: " $(sudo i2cget -y 1 0x3e)
#echo "0x3f: " $(sudo i2cget -y 1 0x3f)
