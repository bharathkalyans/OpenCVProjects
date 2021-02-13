# Learning Basics of Open
# Resources provided by Tech with Tim youtube Channel

import cv2 as cv2

# To import or load a Picture we have to use imread method of cv2 class.

img = cv2.imread('Assets/1.jpeg', 0)

img = cv2.resize(img, (0, 0), fx=0.1, fy=0.2)
# fx and fy are used to shrink or expand the Pixels to make it look bigger or Smaller
# -1 :: cv2.IMREAD_COLOR : ANY TRANSPARENT IMAGE IS LOADED NEGLECTING THE TRANSPARENCY.
# 0 ::  cv2.IMREAD_GRAYSCALE : IN GRAYSCALE MODE
# 1 :: cv2.IMREAD_UNCHANGED : INCLUDING ALPHA CHANNEL

img2 = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

img3 = cv2.imwrite('rotated_image.jpeg', img2)


cv2.imshow('Image Viewer', img2)
cv2.waitKey(0)
# WaitKey Says that you have to wait n sec's to press a key
cv2.destroyAllWindows()
