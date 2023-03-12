#!/bin/bash
./b20.sh
sleep 1
echo "20?: " $(sudo i2cget -y 1 0x3d)
