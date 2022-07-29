from findRedArea import FindRedArea
from mathDistance import MathDistance   # return distance (Maths Distance -> params: Height, camera angle)
from fallTime import FallTime   # return time (Flight time -> params: height)
from distance import Distance   # return distance (Drift distance -> params: velocity, time)
from area import Area           # return redArea, bufferArea (Area Size -> params: NULL)
from speedUAV import SpeedUAV   # return speed (Net Speed -> params: speedUAV, windSpeed)
from gpsArea import GPSArea     # return coordinate (Red Area GPS Coordinate -> params: UavLat, UavLon, Lat, Lon)
from dronekit import connect
from gpsDistance import GPSDistance     # return distance (GPS Distance -> params: UAV GPS, Area GPS)
from readCoordinate import ReadCoordinate

connection_string = "TCP"
uav = connect(ip=connection_string, wait_ready=True, timeout=100, baud=115200)

try:
    cameraAngle = 60
    redArea = FindRedArea(areaRadius=2.5, height=uav.location.global_relative_frame.alt, cameraAngle=cameraAngle, count=50)
    while (redArea.returner()): 
        areaGPS = GPSArea(
            uavLat = uav.location.global_relative_frame.lat,
            uavLon = uav.location.global_relative_frame.lon,
            areaDiffGPS = ReadCoordinate().returner()
        ).returner()

    while(1):
        v = SpeedUAV(
            speed = uav.groundspeed, 
            windSpeed = uav.airspeed
        ).returner()
        
        t = FallTime(
            height = uav.location.global_relative_frame.alt
        ).returner()
        
        x = Distance(
            velocity = v, 
            time = t
        ).returner()

        math_x = MathDistance(
            height = uav.location.global_relative_frame.alt,
            cameraAngle = cameraAngle
        ).returner()
    
        gps_x = GPSDistance(
            uavLat = uav.location.global_relative_frame.lat,
            uavLon = uav.location.global_relative_frame.lon,
            areaGPS = areaGPS 
        ).returner()

        while (x == math_x == gps_x):
            pass #Servo ac

except Exception:
    pass