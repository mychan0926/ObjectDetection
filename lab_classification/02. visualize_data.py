import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
train_dataset=tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_data/',
    image_size=(224,224),
    label_mode='categorical'
)

data = train_dataset.take(1) #data set을 큰덩어리 하나로 가져옴

plt.figure(0) #저장할 그래프
plt.title('data')
for images, labels in data:
    for i in range(25):
        plt.subplot(5,5,i+1) # (그래프를 3*3으로 쪼개서 i+1 선택)
        plt.imshow(images[i].numpy().astype('uint8')) #numpt.astype은 실수를 정수 형태로 변환해준다.
        plt.title(train_dataset.class_names[np.argmax(labels[i])]) # class_names는 파일이름의 배열 :np.argmax 배열에 들어있는 값의 가장 큰 index를 구하는 코드임.
        plt.axis('off')
plt.show()