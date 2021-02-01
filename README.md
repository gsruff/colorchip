# colorchip
## Overview
A simple script to read hex color values from a text file and output solid 'color chip' raster images of each color.
## Dependencies
- [Pillow](https://github.com/python-pillow/Pillow "Pillow")
## Usage
```
usage: colorchip.py [-h] -i FILE [-d DIMENSIONS] [-o OUTPUT] [-f FORMAT]

required arguments:
  -i FILE, --input FILE
                        input file

optional arguments:
  -d DIMENSIONS, --dimensions DIMENSIONS
                        dimensions of generated image in x,y format. default is 100,100.
  -o OUTPUT, --output OUTPUT
                        output path. default is current directory.
  -f FORMAT, --format FORMAT
                        image format. valid options are BMP, GIF, JPEG, and PNG. default is PNG.
```
## Input File
See example 'colors.txt'. Beginning lines with # is also allowed.
