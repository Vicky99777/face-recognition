from PIL import Image, ImageDraw,ImageFilter
#pil is a python imaging library that provides various image processing capabilities.
#Image is a class that represents an image in PIL.
#ImageDraw is a class that provides methods to draw shapes and text on an image.
#we can manipulate images using PIL like resizing, cropping, rotating, filtering, etc.

pil_image = Image.open(r"E:\face-recognition\face-recognition\demo_images\demo1.jpg")
pil_image.show()
image_emboss = pil_image.filter(ImageFilter.EMBOSS())
image_emboss.show() 
#emboss is an image filter that creates a 3D effect by simulating the appearance of raised surfaces.
#imagefilter is object that contains different filters like BLUR,CONTOUR,DETAIL,EDGE_ENHANCE,EDGE_ENHANCE_MORE,EMBOSS,SHARPEN,SMOOTH,Smooth_MORE
image_blur = pil_image.filter(ImageFilter.BLUR())
image_blur.show() 