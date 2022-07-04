from math import sqrt
import math

#? return time (Flight time -> params: height)
class FallTime:
    # height -> UAV height
    # velocity -> Object Drop Velocity
    # heightRedChnl -> Red Channel Ground Clearance
    def __init__(self, height=0, R=0, m=0, heightRedChnl = 100, T=27, velocity=0):
        # Gravitation (m/s2)
        self.g = 9.80665 
        # gram
        self.m = m/1000
        # Temperature
        self.T = T
        # Air Resistance Constant (kg/m3)
        self.K = self.airResistance()
        # Cross Section (m2)
        self.A = math.pi * ((R/2)**2)
        # Height (m)
        self.h = height - heightRedChnl   
        # Velocity (m/s)
        self.v = velocity  
        # Time (s)
        self.t = self.timeCalculator()    

    def airResistance(self):
        mod = self.T % 5
        if mod>=3:
            self.T += (5-mod)
        elif mod<3:
            self.T -= mod
        return self.T

    def limitSpeed(self):
        self.Vlim = sqrt((self.m*self.g)/(self.K*self.A))

    def timeCalculator(self):
        t = ( (-self.v) + sqrt(((self.v)**2) - (4*(self.g/2)*(-self.h))) ) / ( 2*(self.g/2) )
        return t

    def limitTime(self):
        self.t += (self.Vlim - self.v)/self.g

    def returner(self):
        return self.t


