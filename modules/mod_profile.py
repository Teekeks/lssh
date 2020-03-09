import json
from os import makedirs, path, system
from util import get_profile, get_config, show_error, profile_path, profile_stub, get_available_profiles
import argparse


def handle_create(args):
    # create new profile
    print(f'create new profile "{args.name}"...')
    _file = profile_path + args.name + ".json"
    if not path.exists(profile_path):
        makedirs(profile_path)
    if path.exists(_file):
        show_error("profile with that name already exists!")
        return
    with open(_file, "w") as file:
        json.dump(profile_stub, file)
    print('open profile settings: '+_file)
    conf = get_config()
    system(f"{conf['editor']} {_file}")


def handle_show(args):
    _file = profile_path+args.profile+".json"
    if path.exists(_file):
        conf = get_config()
        system(f"{conf['editor']} {_file}")
    else:
        show_error("profile does not exist")


def handle_list(args):
    only_files = get_available_profiles()
    if args.isSimple is not None:
        print(" ".join(only_files))
    else:
        for f in only_files:
            pr = get_profile(f)
            if pr is not None:
                print(f"{f} - {pr['comment']}" if len(pr["comment"]) > 0 else f)


def register_parser(sub: argparse._SubParsersAction):
    group = sub.add_parser('profile', help='manage profiles')
    group.description = 'manage profiles'
    ms = group.add_subparsers(metavar='command')

    show_group = ms.add_parser('show', help='open profile in editor')
    show_group.description = 'open profile in editor'
    show_group.add_argument('profile',
                            metavar='profile',
                            choices=get_available_profiles(),
                            help='the profile to open')
    show_group.set_defaults(func=handle_show)

    list_group = ms.add_parser('list', help='list all available profiles')
    list_group.description = 'list all available profiles'
    list_group.add_argument('isSimple',
                            choices=['simple'],
                            nargs='?',
                            help='display a simple version of this list')
    list_group.set_defaults(func=handle_list)

    create_group = ms.add_parser('create', help='create a new profile')
    create_group.description = 'create a new profile'
    create_group.add_argument('name',
                              type=str,
                              help='the name of the new profile')
    create_group.set_defaults(func=handle_create)
