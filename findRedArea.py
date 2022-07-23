from math import cos, pi, atan
import numpy as np
import cv2

class FindRedArea:
    def __init__(self, cameraAngle=60):
        self.isRed = False
        self.redArea(cameraAngle=cameraAngle)
        self.areaSize = 0

    def radiusArea(self, height=0, size=2.5):
        radian = atan((size/2)/height)
        angle = radian*180/pi*2
        A = ((angle*size/180) ** 2) * pi  # area size -> pi*r2
        return A

    def redArea(self, cameraAngle):
        # Capturing video through webcam
        webcam = cv2.VideoCapture(1)
        self.angle = cameraAngle

        # Start a while loop
        while(1):

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
                # epsilon = 0.001*cv2.arcLength(contour, True)
                # approx = cv2.approxPolyDP(contour, epsilon, True)

                area = cv2.contourArea(contour)

                if( 2000 > area > 600):
                    self.isRed = True
                    x, y, w, h = cv2.boundingRect(contour)
                    imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                    self.areaSize = w*h*pi*cos(self.angle/180*pi)/3779.5275590551   # m of px
                    print(self.areaSize, self.radiusArea(0.6))
                else:
                    self.isRed = False

            # Program Termination
            cv2.imshow("Red Area", imageFrame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break

    def returner(self):
        return self.isRed

FindRedArea()
