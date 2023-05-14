import cv2
import numpy as np
from pyzbar.pyzbar import decode

cam=cv2.VideoCapture(0)
cam.set(3,500)
cam.set(4,500)

while True:
    ret,img=cam.read()
    if not ret:
        break
    img=cv2.flip(img, 1)
    Qrs=decode(img)
    for qr in Qrs:
        pts = np.array([qr.polygon],np.int32)
        cv2.polylines(img,[pts],True,(255,110,220),5)
        print(pts)
        rpts= qr.rect
        cv2.putText(img,qr.data.decode('utf-8'),(rpts[0],rpts[3]),cv2.FONT_HERSHEY_PLAIN,1,(255,000,200),2)
    cv2.imshow('Qr-scan',img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or cv2.getWindowProperty('Qr-scan', cv2.WND_PROP_VISIBLE) < 1:
        cam.release()
        cv2.destroyAllWindows()
    
    