import cv2
import numpy as np

kamera = cv2.VideoCapture(1)

while True:
    ret,kare = kamera.read()
    gri_kare = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    nesne = cv2.imread("nesne.png",0)
    w,h = nesne.shape
    res = cv2.matchTemplate(gri_kare,nesne,cv2.TM_CCOEFF_NORMED) #bu tarama nın yapıldğı komut
    esik_degeri = 0.7
    loc = np.where(res>esik_degeri)
    for n in zip(*loc[::-1]):
        cv2.rectangle(kare,n,(n[0]+h,n[1]+w),(0,255,0),thickness=1) 
    cv2.imshow("ekran",kare)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
kamera.release()
cv2.destroyWindow()