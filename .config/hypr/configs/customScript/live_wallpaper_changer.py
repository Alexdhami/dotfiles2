#!/usr/bin/env python3

import random
import os
import subprocess
import time

    
def get_random_video(live_wallpapers_dir:str):
    if not os.path.exists(live_wallpapers_dir):
        subprocess.run(["notify-send",f"No path -> {live_wallpapers_dir}"])
        exit()

    videos_list = [vid for vid in os.listdir(live_wallpapers_dir) if vid.lower().endswith((".mp4",".mkv",".webm","mov","avi"))]
    if not videos_list:
        subprocess.run(["notify-send","live_wallpaper/video not found."])
        exit()

    random_video = random.choice(videos_list)

    return [random_video.split('.')[0],os.path.join(live_wallpapers_dir,random.choice(videos_list))]

def change_live_wallpaper(full_video_path:str):
    subprocess.run(["pkill", "mpvpaper"])
    time.sleep(0.1)
    subprocess.run(["mpvpaper", "-o","no-audio loop","eDP-1",full_video_path ])

def sendNotification(video_name) -> None:
    if video_name:
        subprocess.run(["notify-send",f"Name: {video_name}"])

def main():
    home_dir = os.path.expanduser("~")
    live_wallpapers_dir = os.path.join(home_dir,"Videos","live_wallpapers")
    video_name,full_video_path = get_random_video(live_wallpapers_dir)
    sendNotification(video_name)
    change_live_wallpaper(full_video_path)

if __name__=="__main__":
    main()
