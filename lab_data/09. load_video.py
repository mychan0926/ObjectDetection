import cv2

path='../data/videos/cabc30fc-e7726578.mov'
cap=cv2.VideoCapture(path) #이미지 프레임 자르기
while cap.isOpened(): #cap이 오픈될동안,
    ret, image = cap.read() #(지금 내가 읽어올 프레임이 있는가),이미지
    if not ret:
        break
    cv2.imshow('video',image) #이미지 프린트 (비디오 자른거)
    if cv2.waitKey(1) == ord('q'):#유한정 대기 q 입력받으면,
        break


cap.release()