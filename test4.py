import cv2
import numpy as np

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, img = cam.read()
    #img = np.zeros( (500,500,3),np.uint8)
    img = cv2.line(img,(0,0),(500,500),(255,0,0),5)
    img = cv2.circle(img,(400,100),50,(0,0,255),-1)
    img = cv2.rectangle(img, (250, 0),(500, 125),(0,255,0),3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'LOL',(10,300),font,1,(255,255,255),1,cv2.LINE_AA )

    cv2.imshow("img",img)

    #cv2.waitKey(0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

