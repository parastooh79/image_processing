import cv2 as cv

# create the face haar cascade
faceCascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")

# read the image
image = cv.imread("mypic.jpg")

# detect face in the image
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
face = faceCascade.detectMultiScale( gray , scaleFactor=1.1 , minNeighbors=5 ,minSize=(30 , 30))

# Draw a rectangle around the face
for (x, y, w, h) in face:
    cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # create the eyes haar cascade
    eyeCascade = cv.CascadeClassifier("parojosG.xml")
    
    # detect eyes in the image
    Eyes = eyeCascade.detectMultiScale( image, scaleFactor=1.1 , minNeighbors=10 )
    
    # Draw a rectangle around the eyes
    for (ex,ey,ew,eh) in Eyes:
        cv.rectangle( image ,(ex,ey),(ex+ew,ey+eh),(255,0,0),5)

cv.imshow("face & eyes detected" , image)
cv.waitKey(0)
