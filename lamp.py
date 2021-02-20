#!/usr/bin/env python3

from yeelight import discover_bulbs

discovered = False

while discovered == False:
    bulb = discover_bulbs()

    if len(bulb) > 0:
        print(bulb)
        discovered=True

# get_prop
# set_default
# set_power
# toggle
# set_bright
# set_rgb
# set_hsv
# start_cf
# stop_cf
# set_scene
# cron_add
# cron_get
# cron_del
# set_ct_abx
# set_adjust
# adjust_bright
# adjust_ct
# adjust_color
# set_music
# set_name