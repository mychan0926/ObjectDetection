import retinanet
import cv2
import yolov3
#model= retinanet.RetinaNet()
model= yolov3.YOLO_V3()
model.build()
model.load()

image=cv2.imread('../data/images/34811fce-1c9200fe.jpg')
result= model.predict(image)
cv2.imshow('result',result)

cv2.waitKey(0)