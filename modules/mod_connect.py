from pprint import pprint
from os import system
from util import get_profile, show_error


def handle(args):
    if len(args) > 0:
        # get profile
        profile = get_profile(args[0])
        if profile is None:
            show_error(f'"{args[0]}" is not a valid profile')
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
        _conn_str += " "+" ".join(args[1:])
        system(_conn_str)
        pass
    else:
        show_error("missing profile name")
    pass
