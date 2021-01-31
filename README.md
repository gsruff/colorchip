# colorchip
## Overview
A simple script to read hex color values from a text file and output solid 'color chip' raster images of each color.
## Dependencies
- [Pillow](https://github.com/python-pillow/Pillow "Pillow")
## Usage
```
    usage: colorchip.py [-h] -i FILE [-d DIMENSIONS]
    
    required arguments:
      -i FILE, --input FILE
                            input file
    
    optional arguments:
      -d DIMENSIONS, --dimensions DIMENSIONS
                            dimensions of generated image in x,y format. default is 100,100.
```
## Input File
See example 'colors.txt'. Beginning lines with # is also allowed.
## Output
Output image files are in PNG format and are saved to the same location as colorchip.py.
