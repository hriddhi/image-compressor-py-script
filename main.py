import sys
import re
import os
from PIL import Image


def parse_command(sys_argv):
    '''
    Function to parse arguments from the command line

    Returns a dict of arguments
    '''

    print("cmd entry: ", cmds := sys_argv)

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


def open_image_file(path):
    if os.path.exists(path) and os.path.isfile(path):
        return Image.open(path)
    else:
        raise FileNotFoundError(f'open_image_file(): file not found: {path}')


def check_output_path(path):
    if os.path.isfile(path):
        overwrite_choice = input(
            'file already exists at output. Overwrite file? (Y/n) ')
        if overwrite_choice.lower() == 'y':
            return True
        elif overwrite_choice.lower() == 'n':
            raise FileExistsError(
                f'check_output_path(): file already exist at output: {path}')
        else:
            raise ValueError(
                f'check_output_path(): invalid choice: {overwrite_choice}')

    return True


def compress_and_save_image(image, path, quality):
    try:
        image.save(path, quality=int(quality), optimize=True)
    except FileNotFoundError as err:
        os.mkdir(os.path.dirname(path))
        image.save(path, quality=int(quality), optimize=True)


if __name__ == '__main__':
    params = parse_command(sys.argv)
    image = open_image_file(params['-i'])
    if check_output_path(params['-o']):
        compress_and_save_image(image, params['-o'], params['-q'])
