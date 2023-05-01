import cv2
import matplotlib.pyplot as plt

fd=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
vid=cv2.VideoCapture(0)
while True:
    flag,img=vid.read()
    if flag:

        #processing
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces=fd.detectMultiScale(img_gray,1.1,5)
        th,img_bw=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)
       # print(type(img_gray))
        #break
        cv2.imshow('Preview',img_bw)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    else:
        print('No frame')
        break
vid.release()
cv2.destroyAllWindows()