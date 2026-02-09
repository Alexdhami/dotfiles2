#!/usr/bin/env bash

bar="▁▂▃▄▅▆▇█"

# Pre-build sed script once
dict="s/;//g;"
for ((i=0; i<${#bar}; i++)); do
    dict="${dict}s/$i/${bar:$i:1}/g;"
done

# Write cava config
config_file="/tmp/polybar_cava_config"

touch $config_file

echo "[general]
bars = 18
framerate = 60

[output]
method = raw
raw_target = /dev/stdout
data_format = ascii
ascii_max_range = 7" >> $config_file

# wait for paulseaudio/pipewire starts
until pactl info >/dev/null 2>&1; do
    sleep 0.2
done

# Use sed once in the pipeline instead of per-line
cava -p "$config_file" | sed -u "$dict"
