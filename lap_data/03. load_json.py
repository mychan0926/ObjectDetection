import json
import cv2
f=open('../data/labels/labels.json')

label = json.load(f)#b001a7ce-5cbc6e0b.jpg

file_name=input()

image= cv2.imread("../data/images/"+ file_name) #이미지 불러오기
for j in range (len(label)):

    for i in range (len(label[j]["labels"])):

        if 'box2d' in label[j]["labels"][i].keys() and file_name in label[j]['name']:
            print(label[j]["labels"][i]['category'],end=' ')
            X1=label[j]["labels"][i]["box2d"]["x1"]
            Y1=label[j]["labels"][i]["box2d"]["y1"]
            X2=label[j]["labels"][i]["box2d"]["x2"]
            Y2=label[j]["labels"][i]["box2d"]["y2"]
            cv2.rectangle(image, (int(X1),int(Y1)),(int(X2),int(Y2)), (255,255,255), 1 )
            cv2.putText(image,label[j]["labels"][i]['category'],(int((int(X1)+int(X2))/2-len(label[j]["labels"][i]['category'])*2.5),int(Y1)-10),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),1)


cv2.imshow("image",image)
cv2.waitKey(0)



