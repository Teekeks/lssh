import json
from pathlib import Path
from os import path
from sys import stderr

##################################################################################
# Profile
##################################################################################

def get_profile(name: str):
    _path = home_path+"profiles/"
    _file = _path+name+".json"
    if not path.exists(_file):
        print(f'ERROR: could not find profile "{name}!')
        return None
    _json = None
    with open(_file, "r") as file:
        _json = json.load(file)
    return _json


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
    "editor": "subl"
}

home_path = str(Path.home())+"/.lssh/"


def get_config():
    _file = home_path + "config.json"
    if not path.exists(_file):
        write_config(default_config)
        return default_config
    with open(_file, "r") as f:
        return json.load(f)


##################################################################################
# Console
##################################################################################

def show_error(msg: str) -> None:
    print(f"ERROR: {msg}", file=stderr)
