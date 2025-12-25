#!/usr/bin/env python3

import random
import os
import subprocess
import sys

home_dir = os.path.expanduser("~")
parentDir = f"{home_dir}/Pictures/Wallpapers/"

try:

    imagesList = [img for img in os.listdir(parentDir) if img.lower().endswith((".png",".jpg",".jpeg"))]

except:
    sys.exit(1)

if not imagesList:
    sys.exit(1)

# List of transitions
transitions = ["fade","wipe","grow","center","outer","any"]
randomImageDir =  parentDir + random.choice(os.listdir(parentDir))

try:
    subprocess.run(["swww", "img","--transition-type",random.choice(transitions),randomImageDir ])
except:
    sys.exit(1)

