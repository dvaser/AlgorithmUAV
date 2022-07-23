import cv2
import numpy as np

webcam = cv2.VideoCapture(1)

while (1):
    # Load the image
    _,img = webcam.read()
    # Convert to greyscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Set range for red color and define mask
    redLower = np.array([136, 87, 111], np.uint8)
    redUpper = np.array([180, 255, 255], np.uint8)
    redMask = cv2.inRange(hsvFrame, redLower, redUpper)

    # Morphological Transform, Dilation for each color and bitwise_and operator between imageFrame and mask determines to detect only that particular color
    kernal = np.ones((5, 5), "uint8")

    # For red color
    redMask = cv2.dilate(redMask, kernal)

    # Convert to binary image by thresholding
    _, threshold = cv2.threshold(redMask, 245, 255, cv2.THRESH_BINARY_INV)
    # Find the cntrs
    cntrs, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # For each contour approximate the curve and
    # detect the shapes.
    for cnt in cntrs:
        epsilon = 0.001*cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        cv2.drawContours(img, [approx], 0, (0), 3)
        # Position for writing text
        x,y = approx[0][0]
    
        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)
        elif len(approx) == 4:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)
        elif len(approx) == 5:
            cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)
        elif 6 < len(approx) < 15:
            cv2.putText(img, "Ellipse", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)
        else:
            cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0,2)
    
    cv2.imshow("Red Area", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break