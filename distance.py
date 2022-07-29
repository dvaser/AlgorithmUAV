
#! Distance with horizontal throw (Speed UAV * Ball Drop Time)
#? return distance (Drift distance -> params: velocity, time)
class Distance:
    def __init__(self, velocity=0, time=0):
        # Velocity (m/s) -> UAV Velocity
        self.v = velocity
        # Time (s) -> Flight time
        self.t = time
        # Distance (m)
        self.x = self.distanceCalculator() 

    # Distance Calculate
    def distanceCalculator(self):
        x = self.v * self.t
        return x

    def returner(self):
        return self.x
