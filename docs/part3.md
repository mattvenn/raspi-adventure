# The Aim

Now we're moving onto images. You now need to create a PNG image, with 3 circles in it. The 3 circles must be red, green and blue.

The image file must be in the directory given in the message, and must be called image.png

# What you'll need to know...

## The python image library

    import Image, ImageDraw

## Creating a new image

    image = Image.new('RGB', size)

where size is a tuple that specifies the width and height of the image:

    (width,heigth)

## The draw object

    draw = ImageDraw.Draw(image)

We can then use this to draw shapes on our image

## Drawing a circle

    draw.ellipse(co-ords, fill=colour)

Where co-ords is a 4 part array that defines the top left of the ellipse and the bottom right of the ellipse.

And color is a 3 part array that specifies the red, green and blue component of the colour we want the ellipse to be.

## Saving the image

    image.save('image.png','PNG')

## Looking at your image

To check your image, you can use winscp (on the usb stick provided at the start of the workshop, or download from here: http://winscp.net/eng/index.php)

You can copy the image from the pi to your laptop and look at it there.

# Further reading

* Images: http://effbot.org/imagingbook/image.htm
* Drawing: http://effbot.org/imagingbook/imagedraw.htm
