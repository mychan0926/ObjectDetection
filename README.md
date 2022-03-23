# RoadObjectDetection


## [자료 조사 & 탐구 동기]


### [탐구 동기]

현재 테슬라, 그 외 다른 자동차 회사들이 개발하고 있는 자율 주행 기술이 어떤 식으로 작동되는지, 그리고,
AI, 즉, 인공지능이 어떻게 물체를 인식하고, 작동하는지에 대해, 궁금증이 들어, 프로젝트에 참여하게 되었다.

###  자율 주행 기술의 등장 배경


자율주행의 개념은 1960년에 벤츠를 중심으로 제안되었고,
70년대 중후반부터 초보적인 연구가 시작되었다.
초기에는 장애물에 대한 인식과 대처 기능을
고려하지 않은 상태로 주행 시험장에서 중앙선이나
차선을 넘지 않는 수준의 기능을 개발하였고,
90년대부터는 비전 기술과 기계학습 기술이
접목되면서 장애물 인식을 적용한 자율주행 기술이
본격적으로 연구되기 시작하였다.
우리나라 도로교통공단 2015년 통계를 보면, 교통사고 전체 원인의 95%
이상이 운전자의 부주의로 인한 과실이다. 이에
따라 운전자의 과실을 최소화해, 교통사고로 인한
인명 손실을 줄이기 위해 자동차 선진국에서는
90년도 초반부터 많은 예산을 투입해 자율주행차 기술의 개발을 지원하고 있다. 

### 4차 산업 혁명

빅 데이터 분석, 인공지능, 로봇공학, 사물인터넷을 중심으로 한 기술 혁신이다.

## 기본 정보

### 언어
아나콘다 python 3.6 가상환경

### 라이브러리

opencv-python==4.5.5.62
tensorflow==2.6.2
matplotlib==3.3.4

###  개발도구

PyCharm

## 개발 로그

#### 2022-01-19

* 자율주행 기술 개념 파악 및 이미지 처리기술을 탐구했다.
* Object Detection을 활용하여, 객체를 구분 할 수 있게 하는 것이 최종 목표이다.

#### 2022-01-24

* 깃허브와 파이참을 이용해, 파일소스를 깃허브에 올리는 방법을 습득 및 계정 생성.
* 이미지 인식을 하기위해 필요한 json 파일 해석 알고리즘을 배워보았다.
* json파일 내에는 이미지 안의 물체들에 대한 정보가 배열과 사전으로 정리되어있어, 그 물체에 대한 정보를 불러오는 방법을 공부했다.
* cv2를 이용해, cv2내의 cv2.imshow() 함수를 통해, 경로를 넣어, 이미지를 출력시킬수 있는 알고리즘을 제작하였다.
* +예제 이미지 다운

#### 2022-01-26

* 24일보다 심화된 해석 알고리즘을 통해, key값과 리스트의 값을 출력했다.
* 또한, 차와 모터등 여러 정보값이 들어있는 json 파일을 기초로,
* 사각형을 그릴수 있는 알고리즘을 만들었다.
* 사각형을 그릴때에도, cv2를 이용하였으며, 내부함수중 cv2.rectangle() 함수를 통해, 사각형을, 
* cv2.putText 함수를 이용해 글자를 출력하였다.


   
   
![noname01](https://user-images.githubusercontent.com/98321404/153199877-33cbebf2-a660-479d-b922-dab9c8070ba1.jpg)

#### 2022-02-07

* 앞서 사각형을 그린 부분을 image[y1:y2,x1:x2]형식으로 잘라서 다른 jpg파일로 저장하였다.
* 이때, os.listdir을 통해 이미지 파일들을 불러오고, os.path.exists를 통하여 파일 유뮤를,
* cv2.imwrite를 통해 이미지 형식으로 저장하였다.   

   
![noname02](https://user-images.githubusercontent.com/98321404/153199888-9ec72d85-75f2-49a6-aee1-6b5fefc75b4e.jpg)


#### 2022-02-09

* tensorflow와 matplotlib를 설치한후, tensorflow의 train_dataset.take(1)을 이용해 큰덩어리로 가져온후,
* for images, labels in data: 코드로 분해한후, 
* (matplotlib.pyplot)(약칭 plt)의 plt.figure()로 그래프를 지정,
* plt.title('data')로 타이틀 이름,
* plt.subplot(5,5,i+1)으로 그래프를 5*5로 쪼개서 i+1번에 삽입 한 후,
* plt.imshow(images[i].numpy().astype('uint8'))를 통해 정수형으로 변환하여,(plt에서는 실수형의 픽셀 색값은 오류가 뜸)
* plt.title(train_dataset.class_names[np.argmax(labels[i])])로 이름을 지정해준후 출력하였다. (plt.axis('off')로 그래프 표기 삭제)   
* 그 결과는 아래와 같이, 자료들을 나누어서 한번에 볼 수 있게 되었다.
   
![캡처](https://user-images.githubusercontent.com/98321404/153203840-dc463da3-f1e1-40a1-b680-77efc5b8ccd8.PNG)


#### 2022-02-14

* 텐서플로우에 내장되어있는, keras 함수를 통하여, 이미 만들어진 가중치등을 적용시킴.
* 인공신경망 합성곱계층과, 완전연결 신경망을 통하여, 데이터를 9개로 압축시킨후, 모델을 저장시킴.
* 

#### 2022-02-16
* 이미지를 보여주면, 그 이미지를 인식하는 코드를 짬.
* 그러나, 아직 학습이 완료되지 않은 상태라, 나오는 출력값은 아무런 예측이 되지 않는 상태임. (사실상 아무것도 배우지 않은사람과 같은 상태)
* resize한 이미지를 텐서플로우의 predict로 판단.

#### 2022-02-23
* 데이터의 로그를 남긴후, 그 로그를 아나콘다를 통하여 시각화함.
* (learning_rate=0.0005)
* ![image](https://user-images.githubusercontent.com/98321404/155313664-fde2757f-2a29-48f6-a909-277d70f8cb09.png)
* (learning_rate=0.01)
* ![image](https://user-images.githubusercontent.com/98321404/155314587-c57c4e10-1016-4b9a-a918-5c1689ffc085.png)
* (learning_rate=0.001)
* ![image](https://user-images.githubusercontent.com/98321404/155315298-68104907-8b37-4900-b630-639b234e42d8.png)

#### 2022-03-02
* GUI 구현 실험을 함.
* ![image](https://user-images.githubusercontent.com/98321404/159701745-c41db2f3-184c-457f-9436-d4a51970ced9.png)
* PyQt5.QtWidgets을 이용해 구현.
#### 2022-03-14
* GUI 구현을 완료함.
* 


가상환경 설정
데이터 수집 (BDD100K)
https://bair.berkeley.edu/blog/2018/05/30/bdd/
데이터 학습
프로그램 제작 (시뮬레이션 환경 - Carla)

anaconda prompt 실행

conda create -n rod-env python=3.6

conda activate rod-env

pip install opencv-python==4.5.5.62

anaconda prompt 실행

conda activate rod-env

pip install tensorflow==2.6.2

pip install matplotlib==3.3.4


