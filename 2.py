#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt
#%%
CAP = cv2.VideoCapture(0)

while 1:
    ret, frame = CAP.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.line(frame, [100, 100], [400, 400], (255, 0, 0), 10)
    cv2.rectangle(frame, [100, 100], [300, 300], (0, 0, 255), 10)
    
    cv2.imshow('g', frame)
    
    if cv2.waitKey(1) and 0xFF == ord ('Q'):
        break

CAP.release()
cv2.destroyAllWindows()
