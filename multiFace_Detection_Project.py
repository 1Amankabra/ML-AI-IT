import cv2
from time import sleep
import face_recognition as fr
import pandas as pd

fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
vid=cv2.VideoCapture(0)
name=input('Enter Your name')
frameLimit=20
frameCount=0
names=[]
enc=[]
while True:
    flag,img=vid.read()
    if flag:

        #processing
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces=fd.detectMultiScale(img_gray,scaleFactor=1.1,minNeighbors=5,minSize=(50,50))
        if len(faces)==1:
            x,y,w,h=faces[0]
            img_face=img[y:y+h,x:x+w,:].copy()
            img_face=cv2.resize(img_face,(400,400),cv2.INTER_CUBIC)
            face_encoding=fr.face_encodings(img_face)
            if len(face_encoding)==1:
                enc.append(face_encoding[0])
                names.append(name)
                frameCount +=1
                if frameCount == frameLimit:
                    break
           # print(face_encoding)

        for x,y,w,h in faces:
            cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(0,0,255),thickness=2)

        cv2.imshow('Preview',img)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    else:
        print('No frames')
        break
    #sleep(0.1)
data={'names':names,'encoding':enc}
pd.DataFrame(data).to_csv('face_data.csv')
cv2.destroyAllWindows()
cv2.waitKey(1)
vid.release()
