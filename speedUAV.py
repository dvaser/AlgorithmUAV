
#? return speed (Net Speed -> params: speedUAV, windSpeed)

class SpeedUAV:
    def __init__(self, speed=0, windSpeed=0):
        self.v = speed
        self.wV = windSpeed
    
    def returner(self):
        return self.v - self.wV