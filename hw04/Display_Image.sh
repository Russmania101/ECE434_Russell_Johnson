#!/bin/bash
# Russell Johnson

# turn on lcd
./on.sh

sleep 2

# display boris image
sudo fbi -noverbose -T 1 -a boris.png

sleep 5

# rotate lcd by 90 degrees
./on_rotate.sh

sleep 2

# display boris image rotated 90 degrees
sudo fbi -noverbose -T 1 -a boris.png

sleep 5

sudo mplayer Sample640.mp4