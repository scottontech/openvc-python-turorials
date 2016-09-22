#Boilerplate Open Image OpenCV Python
#https://scottontechnology.com/open-image-opencv-python/

import cv2

imageSource = 'images/messi5.jpg'
image = cv2.imread(imageSource)

if image is not None:
    cv2.imshow('image',image)

k = cv2.waitKey(0)

cv2.destroyAllWindows()