import cv2
from pyzbar.pyzbar import decode

cam = cv2.VideoCapture(0)
while True:

    ret,frame = cam.read()
    object_detected = decode(frame)

    for i in object_detected:
        print("detected QRcode is : " + i.data.decode('utf-8'))

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
