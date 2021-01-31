import argparse
import re
from PIL import Image

def dims(s):
    try:
        x, y = map(int, s.split(','))
        return x, y
    except:
        raise argparse.ArgumentTypeError('Dimensions must be x,y')

parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument('-i', '--input', dest='file', help='input file',
                    type=argparse.FileType('r'), required=True)
optional.add_argument('-d', '--dimensions',
                    help='dimensions of generated image in x,y format. default is 100,100.',
                    type=dims, default=(100,100))
args = parser.parse_args()

with args.file as colors:
    line_num = 1
    for line in colors:
        color = ''
        if line.startswith('#'):
            color = line[1:-1].strip()
        else:
            color = line.strip()
        hex = re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', color)
        if hex:
            im = Image.new('RGB',args.dimensions,'#' + color)
            # TODO: Add argument to allow specifying output path
            # TODO: Add argument to allow specifying image format
            im.save(color + '.png')
        else:
            print('Hex color code \'{}\' on line {} is invalid.'.format(color,line_num))
        line_num += 1
