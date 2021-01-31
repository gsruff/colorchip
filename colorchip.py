import argparse
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
    for line in colors:
        color = line.strip()
        # TODO: check line for proper hex color value format
        im = Image.new('RGB',args.dimensions,'#' + color)
        im.save(color + '.png')
