from util import write_config, default_config, get_config, home_path, show_error
from pprint import pprint
from os import system


def handle_set(args):
    if len(args) > 1:
        if args[0] in default_config.keys():
            _c = {args[0]: args[1]}
            print(f'setting {args[0]} to "{args[1]}"')
            write_config(_c)
        else:
            show_error(f'{args[0]} is not a valid option')
    else:
        show_error('please specify which config option you want to set')


def handle_show(args):
    if len(args) > 0 and args[0] == "simple":
        print(" ".join(get_config().keys()))
    else:
        pprint(get_config())


def handle_get(args):
    if len(args) > 0:
        if args[0] in default_config.keys():
            c = get_config()
            print(c[args[0]])
        else:
            show_error(f'{args[0]} is not a valid option')
    else:
        show_error('please specify which config option you want to get')


def handle_open(args):
    print('Open config...')
    system(f"{get_config()['editor']} {home_path}config.json")


def handle(args):
    ops = {
        "set": handle_set,
        "get": handle_get,
        "show": handle_show,
        "open": handle_open
    }
    if len(args) > 0:
        op = ops.get(args[0])
        if op is None:
            show_error(f'"{args[0]}" is not a valid option')
            return
        op(args[1:])
    else:
        print("Missing option. Possible:")
        for s in ops.keys():
            print(f"-lssh config {s}")
        show_error("missing option")
        return
