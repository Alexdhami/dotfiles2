#!/usr/bin/env python3

import subprocess

bar="▁▂▃▄▅▆▇█"

mapping = "s/;//g;"
c = 0

while c < len(bar):
    mapping = f"{mapping}s/{c}/{bar[c]}/g;"
    c += 1

config_file="/tmp/polybar_cava_config"

subprocess.run(
    f"cava -p {config_file} | sed -u '{mapping}'",
    shell=True
)

