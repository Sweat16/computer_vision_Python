#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt
#%%
faceXML = cv2.CascadeClassifier("face.xml")
eyeXML = cv2.CascadeClassifier("eye.xml")

CAP = cv2.VideoCapture(0)

while 1:
    _, frame = CAP.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    faces = faceXML.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eyeXML.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,
                          (ex, ey),
                          (ex+ew, ey+eh),
                          (255,255,255), 1)
    cv2.imshow("faces", frame)
        
    if cv2.waitKey(1) and 0xFF == ord ('Q'):
        break

CAP.release()
cv2.destroyAllWindows()
