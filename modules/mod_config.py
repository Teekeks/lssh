from util import write_config


def handle_set(args):
    if len(args) > 1:
        _c = {args[0]: args[1]}
        print(f"setting {args[0]} to '{args[1]}'")
        write_config(_c)
    pass


def handle_show(args):
    pass


def handle(args):
    ops = {
        "set": handle_set,
        "show": handle_show
    }
    if len(args) > 0:
        op = ops.get(args[0])
        if op is None:
            # TODO show error
            return
        op(args[1:])
    else:
        # TODO show error
        return
