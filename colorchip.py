import argparse
import re
import os
from PIL import Image

# define custom argparse types
def dims(s):
    try:
        x, y = map(int, s.split(','))
        return x, y
    except:
        raise argparse.ArgumentTypeError('Dimensions must be x,y')

def writable_dir(s):
    if not os.path.isdir(s):
        raise argparse.ArgumentTypeError('Supplied path {} is not a valid path.'.format(s))
    if os.access(s, os.W_OK):
        return s
    else:
        raise argparse.ArgumentTypeError('Supplied path {} is not writable by the current user.'.format(s))

def image_type(s):
    s = s.lower()
    if s in ['bmp', 'gif', 'jpeg', 'jpg', 'png']:
        return s
    else:
        raise argparse.ArgumentTypeError('Supplied format {} is not valid.'.format(s))

# setup required and optional command line arguments
parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument('-i', '--input', dest='file', help='input file',
                    type=argparse.FileType('r'), required=True)
optional.add_argument('-d', '--dimensions',
                    help='dimensions of generated image in x,y format. default is 100,100.',
                    type=dims, default=(100,100))
optional.add_argument('-o', '--output', help='output path. default is current directory.', type=writable_dir, default=os.getcwd())
optional.add_argument('-f', '--format', help='image format. valid options are BMP, GIF, JPEG, and PNG. default is PNG.',
                        type=image_type, nargs=1, default='PNG')
args = parser.parse_args()

# parse the input file and output images
with args.file as colors:
    line_num = 1
    for line in colors:
        color = ''
        # strip leading # and trailing \n characters
        if line.startswith('#'):
            color = line[1:-1].strip()
        else:
            color = line.strip()
        #  validate hex strings with a regex match
        hex = re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', color)
        if hex:
            im = Image.new('RGB',args.dimensions,'#' + color)
            im.save(args.output + '/' + color + '.' + args.format)
        else:
            print('Hex color code \'{}\' on line {} is invalid.'.format(color,line_num))
        line_num += 1
