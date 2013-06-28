import Image, ImageDraw
size = (100,50)             # size of the image to create
image = Image.new('RGB', size)
draw = ImageDraw.Draw(image)
r = 10
x = 10
y = 10
draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,0,0))
x = 20
y = 20
draw.ellipse((x-r, y-r, x+r, y+r), fill=(0,255,0))
x = 40
y = 30
draw.ellipse((x-r, y-r, x+r, y+r), fill=(0,0,255))
image.save('image.png','PNG')
