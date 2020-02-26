from pprint import pprint
from os import system
from util import get_profile, show_error


def handle(args):
    if len(args) > 0:
        # get profile
        profile = get_profile(args[0])
        if profile is None:
            return
        _conn_str = f"ssh {profile['user']}"
        if len(profile['password']) > 0:
            _conn_str += f":{profile['password']}"
        _conn_str += f"@{profile['ip']} -p {profile['port']}"
        if len(profile['cert_file']) > 0:
            _conn_str += f" -i {profile['cert_file']}"
        system(_conn_str)
        pass
    else:
        show_error("missing profile name")
    pass
