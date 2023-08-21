import cv2 as cv

# to read images
img = cv.imread("photos/cat.jpg")

# to display images
cv.imshow('c',img)

#this line acts as an on click closeing of the window
cv.waitKey(0)