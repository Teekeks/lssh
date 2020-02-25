import json
from pathlib import Path
from os import path


def get_profile(name: str):
    _path = str(Path.home())+"/.lssh/profiles/"
    _file = _path+name+".json"
    if not path.exists(_file):
        print(f'ERROR: could not find profile "{name}!')
        return None
    _json = None
    with open(_file, "r") as file:
        _json = json.load(file)
    return _json


def write_config(conf):
    _file = str(Path.home()) + "/.lssh/config.json"
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


def get_config():
    _file = str(Path.home()) + "/.lssh/config.json"
    if not path.exists(_file):
        write_config(default_config)
        return default_config
    with open(_file, "r") as f:
        return json.load(f)
