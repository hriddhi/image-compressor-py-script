import sys
import re


def parse_command():
    '''
    Function to parse commands
    '''

    print("cmd entry: ", cmds := sys.argv)

    params = {
        '-q': 80
    }

    for i, cmd in enumerate(iterable=cmds, start=0):
        if i == 0:
            continue

        regex = re.compile(r"^[-].+")
        if regex.match(cmd):
            if cmd == "-i" or cmd == "-o" or cmd == "-q":
                params[cmd] = cmds[i+1]
            else:
                raise ValueError(f'parse_command(): invalid argument: {cmd}')

    mandatory_params = ['-i', '-o']
    for param in mandatory_params:
        if param not in params.keys():
            raise ValueError(f'parse_command(): argument not found: {param}')

    return params


if __name__ == '__main__':
    parse_command()
