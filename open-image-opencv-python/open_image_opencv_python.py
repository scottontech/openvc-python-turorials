#https://scottontechnology.com/open-image-opencv-python/

# import the OpenCV package
import cv2

# load the image with imread()
imageSource = 'images/messi5.jpg'
image = cv2.imread(imageSource)

# display the image on screen with imshow()
# after checking that it loaded
if image is not None:
    cv2.imshow('image',image)
elif image is None:
    print ("Error loading image")

# wait time in milliseconds
# this is required to show the image
# 0 = wait indefinitely
k = cv2.waitKey(0)

# close the window
cv2.destroyAllWindows()