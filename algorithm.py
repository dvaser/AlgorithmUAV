import numpy as np
import cv2
from fallTime import FallTime   # return time (Flight time -> params: height)
from distance import Distance   # return distance (Drift distance -> params: velocity, time)
from area import Area           # return redArea, bufferArea (Area Size -> params: NULL)
from speedUAV import SpeedUAV   # return speed (Net Speed -> params: speedUAV, windSpeed)

"""
    ! Hersey nanosaniye (saniye * 10**(-9))

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

try:
    pass
except:
    pass
finally:
    pass

