import cv2
import numpy as np
import handTrackModule as htm
import time
import pyautogui as pag

cap = cv2.VideoCapture(0)
cap.set(3, 640)  
cap.set(4, 480)  


if cap.isOpened() == False:
    print("Error in opening video")
    
detector=htm.handDetector(max=1)
pTime=0
cTime=0

screen_width,screen_height=pag.size()


while True:
    success, img = cap.read()
    img=cv2.flip(img,1)
    if not success:
        print("Failed to capture image")
        continue
    img=detector.findHands(img,draw=False)
    lmList=detector.findPosition(img,draw=False )
    if len(lmList)!=0:
        finger=lmList[8]
        # print(finger)
        cv2.circle(img,(finger[1],finger[2]),10,(255,0,255),-1)
        mouse_x=int(screen_width/img.shape[1]*finger[1])
        mouse_y=int(screen_width/img.shape[0]*finger[2])
        pag.moveTo(mouse_x,mouse_y,duration=0)
        
        thumb=lmList[4]
        # print(thumb)
        cv2.circle(img,(thumb[1],thumb[2]),10,(255,0,255),-1)
        
        
        dist=abs(finger[2]-thumb[2])
        if dist<13 :
            pag.click()
        print(dist)
    cTime=time.time()
    # fps=1/(cTime-pTime)
    # pTime=cTime
    
    if cTime - pTime > 0:
        fps = int(1 / (cTime - pTime))
        pTime = cTime

    
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        
    cv2.imshow('Image', img)
        
    key=cv2.waitKey(1)
    if key==27:
        break
        

cap.release()
cv2.destroyAllWindows() 