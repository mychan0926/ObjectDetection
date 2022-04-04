import cv2
import os

video_name= 'cabc30fc-e7726578.mov'
path='../data/videos/'
cap=cv2.VideoCapture(path+video_name) #이미지 프레임 자르기

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')


if not os.path.exists('../outputs'): #특정경로 확인
    os.mkdir('../outputs')
out=cv2.VideoWriter('../outputs/'+video_name,fourcc,fps,(width, height))
while cap.isOpened(): #cap이 오픈될동안,
    ret, image = cap.read() #(지금 내가 읽어올 프레임이 있는가),이미지
    if not ret:
        break
    cv2.imshow('video',image) #이미지 프린트 (비디오 자른거)
    out.write(image)
    if cv2.waitKey(1) == ord('q'):#유한정 대기 q 입력받으면,
        break


cap.release()
