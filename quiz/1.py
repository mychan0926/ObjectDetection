import cv2
import os
import json
import cv2
f=open('../data/labels/labels.json')

label = json.load(f)#b001a7ce-5cbc6e0b.jpg
listd=os.listdir('../data/images')
for k in range(len(listd)):
    file_name=listd[k]
    count=0

    image= cv2.imread("../data/images/"+ file_name) #이미지 불러오기
    for j in range (len(label)):

        for i in range (len(label[j]["labels"])):

            if 'box2d' in label[j]["labels"][i].keys() and file_name in label[j]['name']:
                count+=1
                X1=label[j]["labels"][i]["box2d"]["x1"]
                Y1=label[j]["labels"][i]["box2d"]["y1"]
                X2=label[j]["labels"][i]["box2d"]["x2"]
                Y2=label[j]["labels"][i]["box2d"]["y2"]

##os.listdir
                cropimage=image[int(Y1):int(Y2)+1,int(X1):int(X2)+1]
                if not os.path.exists("../"+"classification_data/"+label[j]["labels"][i]['category']):  # 특정경로 확인
                    os.mkdir("../"+"classification_data/"+label[j]["labels"][i]['category'])
                cv2.imwrite("../"+"classification_data/"+label[j]["labels"][i]['category']+'/'+listd[k]+" "+str(count)+'.jpg', cropimage)





