import cv2
import os

file_name="00e9be89-00001215.jpg" #파일 이름
image= cv2.imread("../data/images/"+ file_name) #이미지 불러오기
resize_image=cv2.resize(image,(244,244))
if not os.path.exists('abcd'): #특정경로 확인
    os.mkdir('abcd')

cv2.imwrite('abcd/1.jpg',resize_image)
