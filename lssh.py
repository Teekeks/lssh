#!/usr/bin/env python3

import modules.mod_connect as mod_connect
import modules.mod_profile as mod_profile
import modules.mod_config as mod_config
from util import show_error, init
from sys import argv, exit

option_map = {
    "connect": mod_connect.handle,
    "profile": mod_profile.handle,
    "config": mod_config.handle
}

if len(argv) < 2:
    show_error("please specify action")
    exit(1)
action = argv[1]

args = argv[2:]

init()

option = option_map.get(action)
if option is not None:
    option(args)
else:
    show_error('unknown action')
    exit(1)
