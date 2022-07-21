from math import sqrt

class GPSDistance:
    def __init__(self, uavLat=0, uavLon=0, areaLat=0, areaLon=0):
        self.uavLat = uavLat
        self.uavLon = uavLon
        self.areaLat = areaLat
        self.areaLon = areaLon

    def distance(self):
        return sqrt( ((self.uavLat - self.areaLat)**2) / ((self.uavLon - self.areaLon)**2) )

    def returner(self):
        return self.distance()