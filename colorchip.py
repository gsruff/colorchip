from PIL import Image

colors = open('colors.txt', 'r')

colors_list = []
for line in colors:
    colors_list.append(line.strip())
colors.close()

for color in colors_list:
    im = Image.new('RGB',(100,100),'#' + color)
    im.save(color + '.png')
