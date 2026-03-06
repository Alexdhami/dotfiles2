#!/usr/bin/env python3

# Requires to have folder structures like  /home/user/Pictures/Wallpapers/<folder_name>/image.png

import random
import os
import subprocess

def getRandomWallpaperDirName(WallpapersDir:str) :
    if (len(os.listdir(WallpapersDir)) == 0):
        return None
    return os.path.join(WallpapersDir,random.choice(os.listdir(WallpapersDir)))

def changeWallpaper(WallpapersDir:str):
    if not os.path.exists(WallpapersDir):
        subprocess.run(["notify-send",f"No path -> {WallpapersDir}"])
        return

    random_wallpaper =  getRandomWallpaperDirName(WallpapersDir)
    if random_wallpaper is None:
        subprocess.run(["notify-send","No wallpapers Directory inside ",f"{WallpapersDir}/.."])
        return

    imageList = [os.path.join(random_wallpaper,img) for img in os.listdir(random_wallpaper) if img.lower().endswith((".png",".jpg",".jpeg",".webp"))]
    if not imageList:
        subprocess.run(["notify-send","no image found."])
        return

    randomImg = random.choice(imageList)
    transitions = ["fade","wipe","grow","center","outer","any"]
    randomTransition = random.choice(transitions)
    subprocess.run(["swww", "img","--transition-type",randomTransition,randomImg ])
    return os.path.join(random_wallpaper, randomImg)

def sendImageChangedNotification(imgNamePath) -> None:
    if imgNamePath:
        subprocess.run(["notify-send","Wallpaper changed to ",f"{imgNamePath}"])

def main():
    home_dir = os.path.expanduser("~")
    WallpapersDir = os.path.join(home_dir,"Pictures","Wallpapers")
    sendImageChangedNotification(changeWallpaper(WallpapersDir))

if __name__=="__main__":
    main()
