import cv2
import HandTrackingModule as htm
import numpy as np

#webcam accessing commnd

cap=cv2.VideoCapture(0)

detector=htm.handDetector()

draw_color=(0,0,255)
img_canvas = np.zeros((720,1280,3),np.uint8)

while True:
    success,img=cap.read()
    img=cv2.resize(img,(1280,720))
  
    cv2.rectangle(img,pt1=(20,10),pt2=(240,100),color=(0,0,255),thickness=cv2.FILLED)
    cv2.rectangle(img,pt1=(250,10),pt2=(490,100),color=(0,255,0),thickness=cv2.FILLED)
    cv2.rectangle(img,pt1=(500,10),pt2=(720,100),color=(255,0,0),thickness=cv2.FILLED)
    cv2.rectangle(img,pt1=(730,10),pt2=(950,100),color=(0,255,255),thickness=cv2.FILLED)
    cv2.rectangle(img,pt1=(960,10),pt2=(1260,100),color=(255,255,255),thickness=cv2.FILLED)
    cv2.putText(img,text='ERASER',org=(1000,73),fontFace=cv2.FONT_ITALIC,fontScale=1.6,color=(0,0,0),thickness=5)

    img=detector.findHands(img)
    lmlist=detector.findPosition(img)
    if len(lmlist)!=0:
        x1,y1=lmlist[8][1:]
        x2,y2=lmlist[12][1:]
        # print(x1,y1)

#check if fingers are up

        
        fingers = detector.fingersUp()
        # print(fingers)
#selection mode - index and middle finger is up
        if fingers[1] and fingers[2]:
            # print('selection mode')

                xp,yp = 0,0

                if y1 < 100:
                        if 20 < x1 < 240:
                                print('red')
                                draw_color=(0,0,255)

                        elif 250 < x1 < 490:
                                print("blue")
                                draw_color=(0,255,0)
                                
                        elif 500 < x1 < 750:
                                print("green")
                                draw_color=(255,0,0)

                        elif 730 < x1 < 950:
                                print("yellow")
                                draw_color= (0,255,255)
                        else:
                                print('eraser')
                                draw_color=(0,0,0)

                cv2.rectangle (img, (x1,y1),(x2,y2),draw_color,cv2.FILLED)

        
#drawing mode - only index fingrer is up
        if (fingers[1] and not fingers[2]):
                print('drawing mode')

                if xp==0 and yp==0:
                        xp=x1
                        yp=y1
                if draw_color == (0,0,0):
                        cv2.line(img,(xp,yp),(x1,y1),color=draw_color,thickness=50)
                        cv2.line(img_canvas,(xp,yp),(x1,y1),color=draw_color,thickness=50)
                else:
                        cv2.line(img,(xp,yp),(x1,y1),color=draw_color,thickness=10)
                        cv2.line(img_canvas,(xp,yp),(x1,y1),color=draw_color,thickness=10)  #color brush



                xp,yp = x1,y1
        
        img_gray = cv2.cvtColor(img_canvas,cv2.COLOR_BGR2GRAY)
        _,img_inv = cv2.threshold(img_gray,20,255,cv2.THRESH_BINARY_INV)
        img_inv = cv2.cvtColor(img_inv,cv2.COLOR_GRAY2BGR)
        
        
        img = cv2.bitwise_and(img,img_inv)
        img = cv2.bitwise_or(img,img_canvas)

        #add weighted >>>>> for merging
        img = cv2.addWeighted(img,1,img_canvas,0.5,0)



    cv2.imshow('virtual painter',img)
    if cv2.waitKey(1) & 0xFF==27:
       break
cap.release()
cv2.destroyAllWindows()

