
"""
    @Author :   Dogukan Vatansever
    @Links  :   https://linktr.ee/Dvaser 
"""

from findRedArea import FindRedArea     # return isOkay (Find the Red Area -> params: height, cameraAngle, areaRadius, count)
from mathDistance import MathDistance   # return distance (Maths Distance -> params: height, cameraAngle)
from fallTime import FallTime   # return time (Flight time -> params: height)
from distance import Distance   # return distance (Drift distance -> params: velocity, time)
from area import Area           # return redArea, bufferArea (Area Size -> params: None)
from speedUAV import SpeedUAV   # return speed (Net Speed -> params: speedUAV, windSpeed)
from gpsArea import GPSArea     # return coordinate (Red Area GPS Coordinate -> params: uavLat, uavLon, lat, lon)
from dronekit import connect    # connect to UAV
from gpsDistance import GPSDistance     # return distance (GPS Distance -> params: uavGPS, areaGPS)
from readCoordinate import ReadCoordinate   # return lat, lon (Read to Coordinate -> params: None)

# Connect to UAV
connection_string = "COM10"
uav = connect(ip=connection_string, wait_ready=True, timeout=100, baud=115200)

try:
    # Camera Angle
    cameraAngle = 60
    # Find the Red Area
    redArea = FindRedArea(areaRadius=2.5, height=uav.location.global_relative_frame.alt, cameraAngle=cameraAngle, count=1000)
    # Count of find red area, okey?
    while (redArea.returner()): 
        # GPS Coordinate of the Red Area
        areaGPS = GPSArea(
            uavLat = uav.location.global_relative_frame.lat,
            uavLon = uav.location.global_relative_frame.lon,
            areaDiffGPS = ReadCoordinate().returner()
        ).returner()

    while(1):
        # Reel speed of UAV
        v = SpeedUAV(
            speed = uav.groundspeed, 
            windSpeed = uav.airspeed
        ).returner()
        
        # Ball drop time from the UAV to the target
        t = FallTime(
            height = uav.location.global_relative_frame.alt
        ).returner()
        
        # Distance with horizontal throw (Speed UAV * Ball Drop Time)
        x = Distance(
            velocity = v, 
            time = t
        ).returner()

        # Horizontal distance depending on height
        math_x = MathDistance(
            height = uav.location.global_relative_frame.alt,
            cameraAngle = cameraAngle
        ).returner()
    
        # Difference red area coordinate with UAV coordinate 
        gps_x = GPSDistance(
            uavLat = uav.location.global_relative_frame.lat,
            uavLon = uav.location.global_relative_frame.lon,
            areaGPS = areaGPS 
        ).returner()

        # Distance Compare
        while (x == math_x == gps_x):
            pass # Open Servo

except Exception:
    pass