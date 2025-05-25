from PIL import Image, ImageDraw
pil_image = Image.open(r"E:\face-recognition\face-recognition\demo_images\demo1.jpg")
draw = ImageDraw.Draw(pil_image)
draw.rectangle((50, 50, 200, 200), outline=(0,0,0), width=5)
# it selects 50,50 as the top left corner and 200,200 as the bottom right corner of the rectangle.
#outline represents rgb color of the rectangle.

draw.line((50, 50, 552, 600), fill=(255, 0, 255), width=15)
pil_image.show()