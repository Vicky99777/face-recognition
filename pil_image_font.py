#imagefont module
#pi is library and imagefont is a module
from PIL import Image,ImageFont,ImageDraw
pil_image = Image.open(r"E:\face-recognition\face-recognition\demo_images\demo1.jpg")
draw = ImageDraw.Draw(pil_image)
# Load a font and creating a font object
fnt = ImageFont.truetype("arial.ttf", 40)
draw.text((300,800), "this is Aniket ", font=fnt, fill=(255, 0, 0))
pil_image.show()