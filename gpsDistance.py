from math import sqrt

class GPSDistance:
    def __init__(self, uavLat=0, uavLon=0, areaGPS=0):
        self.uavLat = uavLat
        self.uavLon = uavLon
        self.areaLat, self.areaLon = areaGPS

    def distance(self):
        return sqrt( ((self.uavLat - self.areaLat)**2) / ((self.uavLon - self.areaLon)**2) )

    def returner(self):
        return self.distance()