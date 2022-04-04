import tensorflow as tf
import numpy as np
import cv2
import os #폴더 생성용

class Model:
    def __init__(self):
        pass
    # 데이터 불러오기
    def load_data(self):
        self.train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
            '../classification_data/',
            image_size=(224, 224),
            label_mode='categorical'
            # batch_size=1 덩어리를 묶는 기준 (1개씩 묶기)
        )
        self.class_names= self.train_dataset.class_names

    def class_name(self):
        self.train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
            '../classification_data/',
            image_size=(224, 224),
            label_mode='categorical'
            # batch_size=1 덩어리를 묶는 기준 (1개씩 묶기)
        )
        self.class_names = self.train_dataset.class_names
        return self.class_names

    #모델 구축
    def build(self):
        self.model = tf.keras.applications.MobileNet(
            input_shape=(224, 224, 3),
            include_top=False,  # 마지막 분류기준을 없에겠다.
            weights='imagenet'  # 가중치 값은 imagenet을 사용한다.
        )
        self.model.trainable = False
        self.model = tf.keras.Sequential([
            self.model,
            tf.keras.layers.GlobalAveragePooling2D(),  # 7 7을 평균 내는것
            tf.keras.layers.Dense(9),  # 1024개가 9개로 바뀜. #완전연결 신경망
            tf.keras.layers.Softmax()  # 전체의 합으로 배열을 나누어, 전체의 합을 1로 만든다.
        ])

    #모델 학습
    def train(self):
        self.learning_rate = 0.001
        self.model.compile(
            loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
            # loss 데이터 가져오기(값 작아질수록 정확도 업, 오차(틀린 개수)) 이차함수꼴로 그래프가 나온다.
            optimizer=tf.keras.optimizers.RMSprop(learning_rate=self.learning_rate),  # (경사 하강법)줄이는 방법
            metrics=['accuracy']  # 확인하고 싶은 통계값을 보고 싶을 때 쓸 수 있는 함수. (이 코드에선 정확도를 알고 싶어, 정확도로 적음.)
        )
        self.model.fit(self.train_dataset, epochs=20)  # 모델 학습, (데이터셋, 횟수)
    #예측
    def predict(self, path):
        image = cv2.imread(path)
        resize_image = cv2.resize(image, (224, 224))
        data = np.array([resize_image])
        predict = self.model.predict(data)  # 예측
        index = np.argmax(predict)  # 최댓값 (predict (?번지))
        return self.class_names[index]
    #모델 저장
    def save(self):
        if not os.path.exists("../models"):  # 폴더가 그위치에 없다면,
            os.mkdir("../models")  # 만들기
        self.model.save("../models/classification_model.h5")
    #모델 불러오기
    def load(self):
        self.model=tf.keras.models.load_model("../models/savemodel.h5")
    def predict_array(self, path):
        image = cv2.imread(path)
        resize_image = cv2.resize(image, (224, 224))
        data = np.array([resize_image])
        predict = self.model.predict(data)  # 예측
        index = np.argmax(predict)  # 최댓값 (predict (?번지))

        return predict
if __name__ == '__main__':
    model = Model()
    model.load_data()
    model.load()
