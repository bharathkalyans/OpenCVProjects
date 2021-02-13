# Learning Basics of OpenCV
# Resources provided by Tech with Tim youtube Channel

import cv2

# To import or load a Picture we have to use imread method of cv2 class.

img = cv2.imread('Assets/1.jpeg', -1)

img = cv2.resize(img, (800, 400))
# -1 :: cv2.IMREAD_COLOR : ANY TRANSPARENT IMAGE IS LOADED NEGLECTING THE TRANSPARENCY.
# 0 ::  cv2.IMREAD_GRAYSCALE : IN GRAYSCALE MODE
# 1 :: cv2.IMREAD_UNCHANGED : INCLUDING ALPHA CHANNEL


cv2.imshow('Image Viewer', img)
cv2.waitKey(0)
# WaitKey Says that you have to wait n sec's to press a key
cv2.destroyAllWindows()
