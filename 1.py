#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt
#%%
IMAGE = cv2.imread("armin.jpeg", cv2.IMREAD_GRAYSCALE)

#cv2.imshow("G", IMAGE)
plt.imshow(IMAGE, cmap="gray", interpolation="bicubic")
plt.plot([0,640], [0,890], "r", linewidth=0.1)
plt.show()