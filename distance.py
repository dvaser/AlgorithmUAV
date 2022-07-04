
#? return distance (Drift distance -> params: velocity, time)
class Distance:
    # velocity -> UAV Velocity
    # time -> Flight time
    def __init__(self, velocity=0, time=0):
        # Velocity (m/s)
        self.v = velocity
        # Time (s)
        self.t = time
        # Distance (m)
        self.x = self.distanceCalculator() 

    def distanceCalculator(self):
        x = self.v * self.t
        return x

    def returner(self):
        return self.x
