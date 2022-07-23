from findRedArea import FindRedArea
from fallTime import FallTime   # return time (Flight time -> params: height)
from distance import Distance   # return distance (Drift distance -> params: velocity, time)
from area import Area           # return redArea, bufferArea (Area Size -> params: NULL)
from speedUAV import SpeedUAV   # return speed (Net Speed -> params: speedUAV, windSpeed)
from dronekit import connect
from gpsDistance import GPSDistance     # return distance (GPS Distance -> params: UAV GPS, Area GPS)
from mathDistance import MathDistance   # return distance (Maths Distance -> params: Height, camera angle)
from gpsArea import GPSArea     # return coordinate (Red Area GPS Coordinate -> params: UavLat, UavLon, Lat, Lon)


connection_string = "TCP"
uav = connect(ip=connection_string, wait_ready=True, timeout=100, baud=115200)

try:
    while (FindRedArea.returner()):    
        areaGPS = GPSArea(
            uavLat = uav.location.global_relative_frame.lat,
            uavLon = uav.location.global_relative_frame.lon,
            lat = 0,
            lon = 0
        ).returner()
        break

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
            cameraAngle = 60
        ).returner()
    
        gps_x = GPSDistance(
            uavLat = uav.location.global_relative_frame.lat,
            uavLon = uav.location.global_relative_frame.lon,
            areaGPS = areaGPS 
        ).returner()

except:
    pass
finally:
    pass


"""
    ! Saniye cinsinden
    ! Metre cinsinden
    ! Gram cinsinden

    * Raspberry Pi 4 gecikmesi
    ? 1.5 GHz dört çekirdekli ARM Cortex-A72 CPU
    ? 4kp60 HEVC video
    ? 1 × 4K@60Hz veya 2 × 4K@30Hz)

    # Parametre
    * Yukseklik (h)
    * Hiz (V Iha) 
    * Ruzgar (-V ruzgar)
    
    * Yol (x)

    * Kamera fps Hizi 
    * Kamera acisi

    * Alan Konumu (x,y,z)

    * Alan buyuklugu (yaricap hesabi)
    * Guvenli Bolge alani (a*b) - Dikdortgen  

    * Hizlanan, yavaslayan, sabit hareket


"""


#? gHz to s (saniye)
def gHzConvert(gHz):
    s = 1 / gHz * (10**(-3))
    return s

#? fps to m/s
def fpsConvert(fps):
    v = 0.3048 * fps
    return v
