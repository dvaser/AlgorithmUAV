
#! Coordinates save to File 

class Coordinate:
    def __init__(self, areaGPS={0,0}):
        # Difference Red Area Center with Webcam Center
        self.areaLat, self.areaLon = areaGPS
        # Txt File 
        self.filePath = "coordinateDiff.txt"
        # Save gps from .json file
        self.savetoFile()

    def savetoFile(self):
        with open(self.filePath, "a", encoding="utf-8") as file:
            file.write(f"{self.areaLat} {self.areaLon}\n")
