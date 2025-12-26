#!/usr/bin/env python3

import random
import os
import subprocess

    
def changeWallpaper(WallpapersDir:str):

    if not os.path.exists(WallpapersDir):
        subprocess.run(["notify-send",f"No path -> {WallpapersDir}"])
        return
     
    imageList = [img for img in os.listdir(WallpapersDir) if img.lower().endswith((".png",".jpg",".jpeg"))]


    if not imageList:
        subprocess.run(["notify-send","no image found."])
        return

    randomImg = random.choice(imageList)
    imgName = randomImg.split('.')[0]
    fullImgpath = os.path.join(WallpapersDir, randomImg)

    transitions = ["fade","wipe","grow","center","outer","any"]
    randomTransition = random.choice(transitions)
    subprocess.run(["swww", "img","--transition-type",randomTransition,fullImgpath ])
    return imgName

def sendNotification(imgName) -> None:
    if imgName:
        subprocess.run(["notify-send",f"Name: {imgName}"])

def main():
    home_dir = os.path.expanduser("~")
    WallpapersDir = os.path.join(home_dir,"Pictures","Wallpapers")
    imgName = changeWallpaper(WallpapersDir)
    sendNotification(imgName)

if __name__=="__main__":
    main()

