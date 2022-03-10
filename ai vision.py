import cv2

Import pytesseract

Import numpy as np

from PIL Import Image, ImageGrab

import time from

firebase import firebase

cap = cv2.VideoCapture (0) cap. set (3,640)

cap. set (4,480)

def captureScreen(bbox=(300, 300, 1500, 1000)):

capScr= np.array(ImageGrab.grab (bbox))

capScr = cv2.cvtColor (capScr, cv2.COLOR_RGB2BGR)

return capScr

firebase=firebase.FirebaseApplication( "https://smart-image-transport-default-rtd

while True:

print("Ready to go")

custom_config=roen 3psm 6°

timer = cv2.getTickCount()

_img= cap.read()

#ing = captureScreen() #DETECTING CHARACTERES

hing, wing, img.shape

boxes = pytesseract.image_to_boxes (img)

text=pytesseract.image_to_string(1mg, config=custom_config) print (text)

for b in boxes.splitlines():

sprint (b)

b = b.split("")

#print(b)

x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4]) cv2.rectangle(1mg, (x, hImg- y). (w, hImg- h), (50, 50, 255), 2)

cv2.put Text (1mg, b[0], (x, himg- y+25), cv2. FONT HERSHEY SIMPLEX, 1, (50, 50, 255)

fps = cv2.getTickFrequency()/ (cv2.getTickCount() - timer);
for b in boxes.splitlines():

sprint (b)

b = b.split(""

#print (b)

x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4]) cv2.rectangle(img, (x, hImg- y), (w, hImg- h), (50, 50, 255, 2)

cv2.put Text (img, b[0], (x, himg- y+25), cv2.FONT HERSHEY SIMPLEX, 1, (50, 50, 255) fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

cv2.1mshow("Result",img) data_to_upload-("ID": text

firebase.post('/smart-image-transport", data_to_upload) #cv2.put Text (ing, str(int(fps)), (75, 49), cv2.FONT HERSHEY_SIMPLEX, 0.7.

cv2.waitKey (0)