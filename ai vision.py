import cv2
import pytesseract
import numpy as np
import picamera
from PIL import Image, ImageGrab
import time 
from firebase import firebase

cap = cv2.VideoCapture(0)
cap. set (3,640)
cap. set (4,480)

def captureScreen(bbox=(300, 300, 1500, 1000)):
    capScr= np.array(ImageGrab.grab (bbox))
    capScr = cv2.cvtColor (capScr, cv2.COLOR_RGB2BGR)
    return capScr

firebase=firebase.FirebaseApplication('https://smart-image-transport-default-rtdb.firebaseio.com/')

while True:
    print("ready go ")
    custom_config = r'--oem 3 --psm 6'
    timer = cv2.getTickCount()
    _,img = cap.read()
    #img = captureScreen()
    #DETECTING CHARACTERES
    hImg, wImg,_ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    text=pytesseract.image_to_string(img, config=custom_config)
    print (text)
    for b in boxes.splitlines():
        #print(b)
        b = b.split(' ')
        #print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
        cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    cv2.imshow("Results",img)
    data_base={ "iD":text}
    firebase.post('/smart-image-transport', data_base)
    #cv2.putText(img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20,230,20), 2);
    cv2.imshow("Result",img)
    cv2.waitKey(0)

