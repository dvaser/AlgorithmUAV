#? return distance (Maths Distance -> params: height, cameraAngle)

from math import tan, pi

class MathDistance:
    def __init__(self, height=0, cameraAngle=60):
        self.h = height
        self.r = cameraAngle    # Angle with upper base
        self.x = self.calculator()

    # Calculate
    def calculator(self):
        return ( self.h * tan(90-self.r/180*pi) )

    def returner(self):
        return self.x