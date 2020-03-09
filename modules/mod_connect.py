from os import system
from util import get_profile, show_error, get_available_profiles
import argparse


def handle(args):
    # get profile
    profile = get_profile(args.profile)
    if profile is None:
        show_error(f'"{args.profile}" is not a valid profile')
        return
    _conn_str = f"ssh {profile['user']}"
    if len(profile['password_file'] + profile['password']) > 0:
        if len(profile['password_file']) > 0:
            # file takes preference over direct password since its more secure
            _conn_str = f"sshpass -f {profile['password_file']} " + _conn_str
        else:
            _conn_str = f"sshpass -p {profile['password']} " + _conn_str
    _conn_str += f"@{profile['ip']} -p {profile['port']}"
    if len(profile['cert_file']) > 0:
        _conn_str += f" -i {profile['cert_file']}"
    # append all additional params to the ssh connection string
    _conn_str += " "+" ".join([f"'{x}'" if ' ' in x else x for x in args.ssh_args])
    system(_conn_str)


def register_parser(sub: argparse._SubParsersAction):
    group = sub.add_parser('connect')
    group.description = 'Connect to a profile'
    group.add_argument('profile',
                       metavar='profile',
                       choices=get_available_profiles(),
                       help='Name of the profile to connect to')
    group.add_argument('ssh_args',
                       type=str,
                       nargs=argparse.REMAINDER,
                       help='arguments to pass to ssh')
    group.set_defaults(func=handle)
