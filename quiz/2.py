import cv2
import os
import json
import matplotlib.pyplot as plt
file=input()
list=os.listdir("../"+file)
img={}
for i in range(len(list)):

    img[i] = cv2.imread("../"+file+"/"+list[i])
plt.axis("off")