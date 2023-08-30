import cv2 as cv

# to read images
#img = cv.imread("photos/cat_large.jpg")

# to display images
#cv.imshow('c',img)

# to read videos
capture = cv.VideoCapture("videos/billy.mp4")

while True:
    isTrue , frame = capture.read()
    cv.imshow('v', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
#this line acts as an on click closeing of the window

capture.release()
cv.destroyAllWindows()