import cv2
file_name="00e9be89-00001215.jpg" #파일 이름
image= cv2.imread("../data/images/"+ file_name) #이미지 불러오기
resize_image=cv2.resize(image,(1000,200))
cv2.imshow("image",resize_image)
cv2.waitKey(0)