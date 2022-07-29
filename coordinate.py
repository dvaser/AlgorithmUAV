
class Coordinate:
    def __init__(self, areaGPS={0,0}):
        self.areaLat, self.areaLon = areaGPS
        self.filePath = "coordinateDiff.txt"
        #! Save gps from .json file
        self.savetoFile()

    def savetoFile(self):
        with open(self.filePath, "a", encoding="utf-8") as file:
            file.write(f"{self.areaLat} {self.areaLon}\n")
