import cv2
file_name="00e9be89-00001215.jpg" #파일 이름
image= cv2.imread("../data/images/"+ file_name) #이미지 불러오기
cv2.rectangle(image, (300, 300), (100, 100), (0,255,0), 10 ) #사각형 그리기
cv2.imshow("image",image)
cv2.waitKey(0)
