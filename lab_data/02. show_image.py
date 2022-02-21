import cv2
file_name="b001a7ce-5cbc6e0b.jpg" #파일 이름
image= cv2.imread("../data/images/"+ file_name) #이미지 불러오기

cv2.imshow("image",image)
cv2.waitKey(0)