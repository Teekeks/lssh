from util import write_config, default_config, get_config, home_path
from pprint import pprint
from os import system
import argparse


def handle_set(args):
    _c = {args.key: args.value}
    print(f'setting {args.key} to "{args.value}"')
    write_config(_c)


def handle_show(args):
    if args.isSimple is not None:
        print(" ".join(get_config().keys()))
    else:
        pprint(get_config())


def handle_get(args):
    c = get_config()
    print(c[args.option])


def handle_open(args):
    print('Open config...')
    system(f"{get_config()['editor']} {home_path}config.json")


def register_parser(sub: argparse._SubParsersAction):
    group = sub.add_parser('config', help='Show and change settings')
    group.description = 'Show and change settings'
    ms = group.add_subparsers(metavar='command')

    set_group = ms.add_parser('set', help='set the value of a setting')
    set_group.description = 'set the value of a setting'
    set_group.add_argument('key',
                           type=str,
                           choices=default_config.keys(),
                           help='option to set')
    set_group.add_argument('value',
                           help='value you want the option to be')
    set_group.set_defaults(func=handle_set)

    get_group = ms.add_parser('get', help='get the value of a setting')
    get_group.description = 'get the value of a setting'
    get_group.add_argument('option',
                           type=str,
                           choices=default_config.keys(),
                           help='the option you want to get')
    get_group.set_defaults(func=handle_get)

    open_group = ms.add_parser('open', help='open config in editor')
    open_group.description = 'open config in editor'
    open_group.set_defaults(func=handle_open)

    show_group = ms.add_parser('show', help='print config to console')
    show_group.description = 'print config to console'
    show_group.add_argument('isSimple',
                            choices=['simple'],
                            nargs='?',
                            help='only show available settings')
    show_group.set_defaults(func=handle_show)
