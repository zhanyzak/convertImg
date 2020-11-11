from PIL import Image

img = Image.open("image.jpg")
blackAndWhite = img.convert('L')
blackAndWhite.save("bw_image.jpg")
blackAndWhite.show("bw_image.jpg")