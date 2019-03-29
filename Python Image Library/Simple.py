from PIL import Image, ImageOps, ImagePalette
image1 = Image.open('sekiro.png')
image1.show()
image2 = ImageOps.grayscale(image1)
image2.show()
image2.save('sekirogs.png')