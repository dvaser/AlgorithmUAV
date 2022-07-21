from math import sin, pi

class MathDistance:
    def __init__(self, height=0, cameraAngle=60):
        self.h = height
        self.r = cameraAngle
        self.x = self.calculator()

    def calculator(self):
        return (self.h * sin(self.r/180*pi) / sin((90-self.r)/180*pi))

    def returner(self):
        return self.x