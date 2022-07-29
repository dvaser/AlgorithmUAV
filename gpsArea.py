#? return areaLat, areaLon (GPSArea -> params: uavLat, uavLon, areaDiffGPS)

class GPSArea:
    def __init__(self, uavLat=0, uavLon=0, areaDiffGPS={0,0}):
        self.uavLat = uavLat
        self.uavLon = uavLon
        self.lat, self.lon = areaDiffGPS
    
    # Add Difference lat & lon on GPS Lat & Lon
    def GPSRedArea(self):
        self.areaLat = self.uavLat + self.lat
        self.areaLon = self.uavLon + self.lon
        return self.areaLat, self.areaLon

    def returner(self):
        return self.GPSRedArea()