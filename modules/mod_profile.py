from pprint import pprint
import json
from pathlib import Path
from os import makedirs, path, system
from util import get_profile, get_config
from os import listdir
from os.path import isfile, join

profile_stub = {
    "user": "",
    "ip": "",
    "port": 22,
    "password": "",
    "cert_file": "",
    "comment": ""
}


def handle_create(args):
    if len(args) > 0:
        # create new profile
        print(f'create new profile "{args[0]}"...')
        _path = str(Path.home())+"/.lssh/profiles/"
        if not path.exists(_path):
            makedirs(_path)
        if path.exists(_path+args[0]+".json"):
            print("ERROR: profile with that name already exists!")
            return
        with open(_path+args[0]+".json", "w") as file:
            json.dump(profile_stub, file)
        print('open profile settings: '+_path+args[0]+".json")
        conf = get_config()
        system(f"{conf['editor']} {_path}{args[0]}.json")
        # system(f"subl {_path}{args[0]}.json")
    else:
        print("ERROR: missing profile name")


def handle_show(args):
    if len(args) > 0:
        _path = str(Path.home()) + "/.lssh/profiles/"
        _file = _path+args[0]+".json"
        if path.exists(_file):
            conf = get_config()
            system(f"{conf['editor']} {_file}")
        else:
            print("ERROR: profile does not exist")
    else:
        print("ERROR: missing profile name")


def handle_list(args):
    _path = str(Path.home())+"/.lssh/profiles/"
    onlyfiles = [path.splitext(f)[0] for f in listdir(_path) if isfile(join(_path, f))]
    for f in onlyfiles:
        pr = get_profile(f)
        if pr is not None:
            print(f"{f} - {pr['comment']}" if len(pr["comment"]) > 0 else f)
    pass


def handle(args):
    options = {
        "show": handle_show,
        "create": handle_create,
        "list": handle_list
    }
    if len(args) == 0:
        print("Missing option. Possible:")
        for s in options.keys():
            print(f"-lssh profile {s}")
    else:
        opt = options.get(args[0])
        if opt is not None:
            opt(args[1:])
        else:
            print("Unknown option. Possible:")
            for s in options.keys():
                print(f"-lssh profile {s}")
