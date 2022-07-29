from math import sqrt
import math

#! Ball drop time from the UAV to the target
#? return time (Flight time -> params: height)
class FallTime:
    # height -> UAV height (m)
    # velocity -> Object Drop Velocity (m/s)
    # heightRedChnl -> Red Channel Ground Clearance (m)
    def __init__(self, height=0, R=0, m=140, heightRedChnl = 0.1, T=27, velocity=0):
        # Gravitation (m/s2)
        self.g = 9.80665 
        # gram
        self.m = m
        # Temperature
        self.T = T
        # Air Resistance Constant (kg/m3)
        self.K = self.airResistance()
        # Ball Cross Section (m2)
        self.A = math.pi * ((R/2)**2)
        # UAV Height (m)
        self.h = height - heightRedChnl   
        # Ball Velocity (m/s)
        self.v = velocity 
        # Fall Time (s)
        self.t = self.timeCalculator()
        # Terminal Velocity (m/s)
        self.Vlim = self.limitSpeed()   

    def airResistance(self):
        # Pascal (Pa)
        self.Pa = .101325
        # K (kg/m3)
        return ( self.Pa / (287.052 * (self.T + 273.15)) )

    # Limit speed 
    def limitSpeed(self):
        return sqrt((self.m*self.g)/(self.K*self.A))

    # Fall time
    def timeCalculator(self):
        """
        if (self.v > self.Vlim):
            return sqrt(2*self.h/self.g)
        else: # Must Make Limit Speed Calculate
            return sqrt(2*self.h/self.g)
        """
        return sqrt(2*self.h/self.g)

    def returner(self):
        return self.t


