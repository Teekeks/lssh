from pprint import pprint
import json
from pathlib import Path
from os import makedirs, path, system
from util import get_profile, get_config, show_error, profile_path, profile_stub
from os import listdir
from os.path import isfile, join


def handle_create(args):
    if len(args) > 0:
        # create new profile
        print(f'create new profile "{args[0]}"...')
        _file = profile_path + args[0] + ".json"
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
    else:
        show_error("missing profile name")


def handle_show(args):
    if len(args) > 0:
        _file = profile_path+args[0]+".json"
        if path.exists(_file):
            conf = get_config()
            system(f"{conf['editor']} {_file}")
        else:
            show_error("profile does not exist")
    else:
        show_error("missing profile name")


def handle_list(args):
    onlyfiles = [path.splitext(f)[0] for f in listdir(profile_path) if isfile(join(profile_path, f))]
    if len(args) > 0 and args[0] == "simple":
        print(" ".join(onlyfiles))
    else:
        for f in onlyfiles:
            pr = get_profile(f)
            if pr is not None:
                print(f"{f} - {pr['comment']}" if len(pr["comment"]) > 0 else f)


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
