import face_recognition

photoDemo1 = face_recognition.load_image_file(r"E:\face-recognition\face-recognition\demo_images\demo1.jpg", "RGB")
photoDemo2 = face_recognition.load_image_file(r"E:\face-recognition\face-recognition\demo_images\demo2.jpg", "RGB")
photoDemo3 = face_recognition.load_image_file(r"E:\face-recognition\face-recognition\demo_images\demo3.jpg", "L")     
photDemo4 = face_recognition.load_image_file(r"E:\face-recognition\face-recognition\demo_images\demo4.jpg", )
print("printing the face encodings and shapes of the images")
#mentioning rgb make sures that the images are loaded in RGB format
#L means that the image is loaded in grayscale format(black and white)
#we dint load photoDemo4 in RGB format because it is already in RGB format
#shape returns the dimensions of the image in the form of (height, width, channels) like (720*1280*3)
print("demo1 shape: ", photoDemo1.shape)
print("demo2 shape: ", photoDemo2.shape)   #demo2 shape:  (920, 736, 3)
print("demo3 shape: ", photoDemo3.shape) #demo3 shape:  (567, 449)
print("demo4 shape: ", photDemo4.shape) #demo4 shape:  (1017, 736, 3)