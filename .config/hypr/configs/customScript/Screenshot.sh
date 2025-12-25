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
    FILENAME="$SCREENSHOT_DIR/area_$(date +%Y-%m-%d_%H-%M-%S).png"
    grim -g "$(slurp)" "$FILENAME" && wl-copy < "$FILENAME" && canberra-gtk-play -i camera-shutter
else
    # Full screen screenshot
    FILENAME="$SCREENSHOT_DIR/screen_$(date +%Y-%m-%d_%H-%M-%S).png"
    grim "$FILENAME" && wl-copy < "$FILENAME" && canberra-gtk-play -i camera-shutter
fi
