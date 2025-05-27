from PIL import Image
import face_recognition #image is class from PIL library
demo = face_recognition.load_image_file(r"E:\face-recognition\face-recognition\demo_images\demo3.jpg")
#image.open() is a method of Image class which open image from path provided
print(demo.shape)
pil_image_of_demo = Image.fromarray(demo)
print(pil_image_of_demo.size)  #size returns the dimensions of the image in the form of (width, height)
pil_image_of_demo.show()  #show method of Image class displays the image in a window
#face_locations is method of face_recognition module which returns the locations of faces in the image
#it returns a list of tuples where each tuple contains the coordinates of the face in the form of (top, right, bottom, left)
#len(face_locations) returns the number of faces found in the image
l = face_recognition.face_locations(demo)
print(l)