import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2
train_dataset=tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_data/',
    image_size=(224,224),
    label_mode='categorical'
)

data = train_dataset.take(1) #data set을 큰덩어리 하나로 가져옴

plt.figure(0) #저장할 그래프
plt.title('data')



model=tf.keras.models.load_model("../models/classification_model_trained.h5")
class_names=['bike', 'bus', 'car', 'motor', 'person', 'rider', 'traffic light', 'traffic sign', 'truck']

for images, labels in data:
    for i in range(25):

        resize_image = cv2.resize(images[i].numpy().astype('uint8'), (224, 224))
        data1 = np.array([resize_image])
        predict = model.predict(data1)  # 예측
        index = np.argmax(predict)  # 최댓값 (predict (?번지))
        axes = plt.gca()
        axes.title.set_size(10)
        plt.subplot(5, 5, i + 1)  # (그래프를 3*3으로 쪼개서 i+1 선택)


        plt.imshow(images[i].numpy().astype('uint8')) #numpt.astype은 실수를 정수 형태로 변환해준다.
        plt.title("true name: "+train_dataset.class_names[np.argmax(labels[i])]+"\n"+"predict name: "+class_names[index]) # class_names는 파일이름의 배열 :np.argmax 배열에 들어있는 값의 가장 큰 index를 구하는 코드임.
        print(index)
        plt.axis('off')
axes = plt.gca()
axes.title.set_size(10)


plt.show()