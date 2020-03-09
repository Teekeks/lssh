import json
from pathlib import Path
from os import path, listdir
from sys import stderr, exit
from os.path import isfile, join


##################################################################################
# Profile
##################################################################################

profile_stub = {
    "user": "",
    "ip": "",
    "port": 22,
    "password": "",
    "cert_file": "",
    "password_file": "",
    "comment": ""
}


def get_profile(name: str):
    _file = profile_path+name+".json"
    if not path.exists(_file):
        show_error(f'could not find profile "{name}!')
        return None
    _json = None
    try:
        with open(_file, "r") as file:
            _json = json.load(file)
            profile = profile_stub.copy()
            profile.update(_json)
        return profile
    except json.decoder.JSONDecodeError:
        show_error(f'While reading profile "{name}": invalid JSON')


def get_available_profiles():
    only_files = [path.splitext(f)[0] for f in listdir(profile_path) if isfile(join(profile_path, f))]
    return only_files

##################################################################################
# Config
##################################################################################

def write_config(conf):
    _file = home_path + "config.json"
    _curr_conf = None
    if path.exists(_file):
        with open(_file, "r") as f:
            _curr_conf = json.load(f)
    if _curr_conf is not None:
        _curr_conf.update(conf)
    else:
        _curr_conf = conf
    with open(_file, "w") as f:
        json.dump(_curr_conf, f)


default_config = {
    "editor": "nano",
    "profile_path": "{lssh_home}profiles/"
}

home_path = str(Path.home())+"/.lssh/"
profile_path = home_path + "profiles/"


def get_config():
    _file = home_path + "config.json"
    if not path.exists(_file):
        write_config(default_config)
        return default_config
    try:
        with open(_file, "r") as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        show_error("while reading config: invalid JSON")
        return default_config


##################################################################################
# Init
##################################################################################

def init():
    global profile_path
    c = get_config()
    profile_path = c["profile_path"].replace("{lssh_home}", home_path)


##################################################################################
# Console
##################################################################################

def show_error(msg: str) -> None:
    print(f"ERROR: {msg}", file=stderr)
    exit(1)
