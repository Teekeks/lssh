#!/usr/bin/env python3

import argparse
import modules.mod_connect as mod_connect
import modules.mod_profile as mod_profile
import modules.mod_config as mod_config
from util import init


parser = argparse.ArgumentParser(
    description="Lena SSH - Manage SSH connections"
)

subparsers = parser.add_subparsers(metavar='command')
mod_config.register_parser(subparsers)
mod_connect.register_parser(subparsers)
mod_profile.register_parser(subparsers)

init()
args = parser.parse_args()
args.func(args)
