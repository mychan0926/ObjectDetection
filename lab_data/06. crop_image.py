import cv2

file_name="3b59c8a5-f0b031cc.jpg" #파일 이름
image= cv2.imread("../data/images/"+ file_name) #이미지 불러오기
cropimage=image[10:100,10:1000] #이미지 자르기
cv2.imshow("image",image) #이미지 출력
cv2.imshow("cropimage",cropimage) #이미지 출력
cv2.waitKey(0)