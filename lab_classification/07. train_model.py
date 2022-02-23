import tensorflow as tf
import os
train_dataset=tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_data/',
    image_size=(224,224),
    label_mode='categorical'
    #batch_size=1 덩어리를 묶는 기준 (1개씩 묶기)
)

model=tf.keras.models.load_model("../models/savemodel.h5")


learning_rate=0.0001
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True), #loss 데이터 가져오기(값 작아질수록 정확도 업, 오차(틀린 개수)) 이차함수꼴로 그래프가 나온다.
    optimizer=tf.keras.optimizers.RMSprop(learning_rate=learning_rate), # (경사 하강법)줄이는 방법
    metrics=['accuracy'] #확인하고 싶은 통계값을 보고 싶을 때 쓸 수 있는 함수. (이 코드에선 정확도를 알고 싶어, 정확도로 적음.)
)
model.fit(train_dataset,epochs=80) #모델 학습, (데이터셋, 횟수)
if not os.path.exists("../models"): #폴더가 그위치에 없다면,
    os.mkdir("../models") #만들기
model.save("../models/savemodel.h5")