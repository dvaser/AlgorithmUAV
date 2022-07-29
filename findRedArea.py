from math import cos, pi, atan
from operator import ifloordiv
import numpy as np
from coordinate import Coordinate
from mathDistance import MathDistance   # return distance (Maths Distance -> params: Height, camera angle)
import cv2

class FindRedArea:
    def __init__(self, height=0, cameraAngle=60, areaRadius=2.5, count = 100):
        self.isOkay = True
        self.redArea(height=height ,cameraAngle=cameraAngle, areaRadius=areaRadius, count=count)
        self.countRed = 0
        self.areaSize = 0
        self.areaGPS = 0,0

    def radiusArea(self, height=0, size=2.5, cameraAngle=60):
        if height != 0: radian = atan((size/2)/height); angle = radian*180/pi*2
        else: angle = 180
        return (((size*angle/180)/2) ** 2) * pi #* cos(cameraAngle*pi/180) # area size -> pi*r2

    def redArea(self, height=0, cameraAngle=60, areaRadius=2.5, count=1000):
        # Capturing video through webcam
        webcam = cv2.VideoCapture(1)

        hFrame,wFrame,__ = webcam.read()[1].shape
        countRed = 0
        # Start a while loop   
        while(1):
            
            if(countRed > count):
                self.isOkay = False
                webcam.release()
                cv2.destroyAllWindows()
                break

            # Reading the video from the webcam in image frames
            _, imageFrame = webcam.read()
            
            # Convert the imageFrame in BGR(RGB color space) to HSV(hue-saturation-value) color space
            hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

            # Set range for red color and define mask
            redLower = np.array([136, 87, 111], np.uint8)
            redUpper = np.array([180, 255, 255], np.uint8)
            redMask = cv2.inRange(hsvFrame, redLower, redUpper)

            # Morphological Transform, Dilation for each color and bitwise_and operator between imageFrame and mask determines to detect only that particular color
            kernal = np.ones((5, 5), "uint8")

            # For red color
            redMask = cv2.dilate(redMask, kernal)

            # Creating contour to track red color
            contours, hierarchy = cv2.findContours(redMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for pic, contour in enumerate(contours):
                epsilon = 0.001*cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)

                area = cv2.contourArea(approx)
                areaReelSize = self.radiusArea(height=height, size=areaRadius, cameraAngle=cameraAngle)*(3779.5275590551**2) 
                
                if(area > 300):
                #if(areaReelSize+100 > (area) > areaReelSize-100):
                    x, y, w, h = cv2.boundingRect(contour)
                    imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    
                    xRedArea = x + int(w/2)
                    yRedArea = y + int(h/2)
                    
                    cv2.circle(imageFrame, (xRedArea, yRedArea), 2, (0, 255, 0), 4)
                    cv2.circle(imageFrame, (int(wFrame/2), int(hFrame/2)), 2, (0, 255, 0), 4)
                    cv2.line(imageFrame, (xRedArea, yRedArea), (int(wFrame/2), int(hFrame/2)), (255,0,0), 2)

                    self.areaGPS = self.latLonCalculator(height=height, x=xRedArea-int(wFrame/2)/(3779.5275590551), y=yRedArea-int(hFrame/2)/(3779.5275590551), cameraAngle=cameraAngle)
                    countRed += 1
                    point = Coordinate(areaGPS=self.areaGPS)

            # Program Termination
            cv2.imshow("Red Area", imageFrame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break

    def latLonCalculator(self, height=0, x=0, y=0, cameraAngle=60):
        lonDiff = MathDistance(height=height, cameraAngle=cameraAngle).returner()
        try:
            latDiff = (x*lonDiff)/y
        except Exception:
            latDiff = 0

        return latDiff, lonDiff

    def returner(self):
        return self.isOkay

# redArea = FindRedArea(areaRadius=0.09, height=0.6, cameraAngle=60, count=50)
