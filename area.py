import math

#! Area Size Calculator
#? return redArea, bufferArea (Area Size -> params: NULL)
class Area:
    def __init__(self, width=25, height=10, R=2.5, x=0, y=0):
        # Area Coordinate
        self.x = x
        self.y = y

        self.pi = math.pi

        # Area Width & Height 
        self.w = width
        self.h = height
        
        # Area Diameter
        self.R = R
        
        # Area Size
        self.redArea = self.redAreaCalculator()
        self.bufferArea = self.bufferAreaCalculator()

    # Red Area Size
    def redAreaCalculator(self):
        rA = self.pi * ( (self.R/2)**2 )
        return rA

    # Buffer Area Size
    def bufferAreaCalculator(self):
        bA = self.w * self.h
        return bA

    def returner(self):
        return self.redArea, self.bufferArea