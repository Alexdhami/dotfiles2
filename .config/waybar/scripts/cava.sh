#!/usr/bin/env bash

bar="▁▂▃▄▅▆▇█"

# Pre-build sed script once
dict="s/;//g;"
for ((i=0; i<${#bar}; i++)); do
    dict="${dict}s/$i/${bar:$i:1}/g;"
done

# Write cava config
config_file="polybar_cava_config"

# Use sed once in the pipeline instead of per-line
cava -p "$config_file" | sed -u "$dict"
