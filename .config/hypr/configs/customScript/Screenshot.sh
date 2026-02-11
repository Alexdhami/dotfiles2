#!/bin/bash

# Screenshot directory
SCREENSHOT_DIR="$HOME/Pictures/Screenshots"

# Check if directory exists, create if it doesn't
if [ ! -d "$SCREENSHOT_DIR" ]; then
    mkdir -p "$SCREENSHOT_DIR"
fi

# Check if it's an area screenshot (argument passed)
if [ "$1" = "area" ]; then
    # Area selection screenshot
    hyprshot  -o $SCREENSHOT_DIR -m region 
    paplay /usr/share/sounds/freedesktop/stereo/camera-shutter.oga

else
    # perticular application
    hyprshot -o $SCREENSHOT_DIR -m window
    paplay /usr/share/sounds/freedesktop/stereo/camera-shutter.oga
fi
