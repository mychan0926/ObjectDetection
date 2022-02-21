import tensorflow as tf
import numpy as np
import cv2
file_name=input()
data_name=input()
model=tf.keras.models.load_model("../../models/mymodel.h5")
class_names=['bike', 'bus', 'car', 'motor', 'person', 'rider', 'traffic light', 'traffic sign', 'truck']

image=cv2.imread("../"+file_name+"/"+data_name)
resize_image=cv2.resize(image,(224,224))
print(resize_image.shape)#(224,224,3)
data=np.array([resize_image])
print(data.shape) #이미지는 배열 형식으로 넣어줘야함.  (1,224,224,3)

predict = model.predict(data) #예측
print(predict) #예측

index=np.argmax(predict) # 최댓값 (predict (?번지))
print(class_names[index])

cv2.imshow("image",resize_image)
cv2.waitKey(0)