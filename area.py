import math

#? return redArea, bufferArea (Area Size -> params: NULL)
class Area:
    def __init__(self, width=25, height=10, R=2.5):
        self.pi = math.pi
        self.w = width
        self.h = height
        self.R = R
        self.redArea = self.redAreaCalculator()
        self.bufferArea = self.bufferAreaCalculator()

    def redAreaCalculator(self):
        rA = self.pi * ( (self.R/2)**2 )
        return rA

    def bufferAreaCalculator(self):
        bA = self.w * self.h
        return bA

    def returner(self):
        return self.redArea, self.bufferArea