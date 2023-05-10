import cv2
import matplotlib.pyplot as plt
from time import sleep
import numpy as np

#for face recognization
fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#for smile recognization
sd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
#video start(camera)
vid=cv2.VideoCapture(0)

notCaptured=True
seq=0
while notCaptured:
    flag,img=vid.read()  #read the image
    if flag:

        #processing
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        #face detect in form
        faces=fd.detectMultiScale(img_gray,scaleFactor=1.1,minNeighbors=5,minSize=(180,180))
       

        np.random.seed(50)
        colors=np.random.randint(0,255,(len(faces),3)).tolist() 
        i=0
        for x,y,w,h in faces:
            #coordinations 
            face=img_gray[y:y+h,x:x+w].copy()
            smiles=sd.detectMultiScale(face,scaleFactor=1.1,minNeighbors=5,minSize=(20,20))
            
            if len(smiles)==1:
                seq+=1
                if seq==5:
                    cv2.imwrite("myselfie.png",img)
                    notCaptured=False
                    break
            else:
                seq=0

            cv2.rectangle(
                img,pt1=(x,y),pt2=(x+w,y+h),color=colors[i]
            )
            i+=1


        cv2.imshow('Preview',img)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    else:
        print('No frame')
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows()