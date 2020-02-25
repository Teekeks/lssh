#!/usr/bin/env python3

from pathlib import Path
import argparse
import modules.mod_connect as mod_connect
import modules.mod_profile as mod_profile
import modules.mod_config as mod_config

argparser = argparse.ArgumentParser(description='Manage ssh connections')
argparser.add_argument('action',
                       metavar='action',
                       type=str,
                       choices=['connect', 'profile', 'config'])
argparser.add_argument('arg', metavar='arg', type=str, nargs='*')
args = argparser.parse_args()

option_map = {
    "connect": mod_connect.handle,
    "profile": mod_profile.handle,
    "config": mod_config.handle
}

option = option_map.get(args.action)
if option is not None:
    option(args.arg)
else:
    print('ERROR: unknown action')