
class ReadCoordinate:
    def __init__(self):
        self.filePath = "coordinateDiff.txt"

    def readCoordinate(self):
        Lat = []
        Lon = []

        with open(self.filePath, "r", encoding="utf-8") as file:
            file.seek(0)

            num = ''
            for i in file.read():
                if(i == '\n'):
                    Lon.append(float(num))
                    num = ''
                    continue
                elif(i == ' '):
                    Lat.append(float(num))
                    num = ''
                    continue
                else:
                    num += (i)

        # txt dosyasina yaz oradan dondur
        return (sum(Lat)/len(Lat)), (sum(Lon)/len(Lon))

    def returner(self):
        return self.readCoordinate()