#!/bin/bash
#
export PRUN=1
export TARGET=pwm5
echo PRUN=$PRUN
echo TARGET=$TARGET

# Configure the PRU pins based on which Beagle is running
machine=$(awk '{print $NF}' /proc/device-tree/model)
echo -n $machine
if [ $machine = "Black" ]; then
    echo " Found"
    pins="P9_31 P9_29 P9_30 P9_28"
elif [ $machine = "Blue" ]; then
    echo " Found"
    pins=""
elif [ $machine = "PocketBeagle" ]; then
    echo " Found"
    pins="P1_36 P1_33 P2_32 P2_30"
elif [ $machine = "Wireless" ]; then
    echo " Found"
    pins="P8_43 P8_44 P8_45 P8_46"
else
    echo " Not Found"
    pins=""
fi

for pin in $pins
do
    echo $pin
    config-pin $pin pruout
    config-pin -q $pin
done
