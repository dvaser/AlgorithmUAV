import cv2
import numpy as np

webcam = cv2.VideoCapture(1)

while (1):
    # Load the image
    _,pic = webcam.read()
    # Convert to greyscale

    hsvFrame = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)

    # Set range for red color and define mask
    redLower = np.array([136, 87, 111], np.uint8)
    redUpper = np.array([180, 255, 255], np.uint8)
    redMask = cv2.inRange(hsvFrame, redLower, redUpper)

    # Morphological Transform, Dilation for each color and bitwise_and operator between imageFrame and mask determines to detect only that particular color
    kernal = np.ones((5, 5), "uint8")

    # For red color
    redMask = cv2.dilate(redMask, kernal)

    gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY) 

    canny = cv2.Canny(redMask,75,105)
    circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 100,param1=100,param2=33,minRadius = 20,maxRadius=200)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]: 
            cv2.circle(pic,(i[0],i[1]),i[2],(0,255,0),5,1)
    

    cv2.imshow("Red Area", pic)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break