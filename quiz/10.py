from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel,QHBoxLayout,QVBoxLayout, QGroupBox,QFileDialog
from PyQt5.QtGui import QPixmap
import sys
import model
import os
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.image_label=QLabel(self)
        self.model = model.Model()

        self.modelnames=self.model.class_name()
        print(self.modelnames)
        self.setWindowTitle('이미지 분류 AI')

        self.button1=  QPushButton('데이터 불러오기')
        self.button2 = QPushButton('모델 학습')
        self.button3 = QPushButton('모델 저장')
        self.button4 = QPushButton('모델 불러오기')
        self.button5 = QPushButton('이미지 예측')
        self.button6 = QPushButton('이미지 불러오기')
        self.group_box1 = QGroupBox("메뉴")
        self.group_box2 = QGroupBox("이미지")
        self.group_box3 = QGroupBox("분류 예측")
        self.button1.clicked.connect(self.button1_click)
        self.button2.clicked.connect(self.button2_click)
        self.button3.clicked.connect(self.button3_click)
        self.button4.clicked.connect(self.button4_click)
        self.button5.clicked.connect(self.button5_click)
        self.button6.clicked.connect(self.button6_click)
        self.text_label = QLabel(self)
        self.text_label.setText('')
        self.button5.setEnabled(False)
        self.hbox_layout=   QHBoxLayout()
        self.v1box_layout = QVBoxLayout()
        self.v2box_layout = QVBoxLayout()

        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)
        self.hbox_layout.addWidget(self.button3)
        self.hbox_layout.addWidget(self.button4)
        self.hbox_layout.addWidget(self.button5)
        self.hbox_layout.addWidget(self.button6)
        self.v2box_layout.addWidget(self.text_label)
        self.v1box_layout.addWidget(self.image_label)
        self.group_box1.setLayout(self.hbox_layout)
        self.group_box2.setLayout(self.v1box_layout)
        self.group_box3.setLayout(self.v2box_layout)
        self.main_layout=QGridLayout()
        self.main_layout.addWidget(self.group_box1,0,0,1,2)
        self.main_layout.addWidget(self.group_box2, 1, 0, 5, 1)
        self.main_layout.addWidget(self.group_box3, 1, 1, 5, 1)
        self.setLayout(self.main_layout)


    def button1_click(self):
        self.button1.setEnabled(False)
        self.model.load_data()
    def button2_click(self):
        self.button2.setEnabled(False)
        self.model.train()
    def button3_click(self):
        self.button3.setEnabled(False)
        self.model.save()
    def button4_click(self):
        self.button4.setEnabled(False)
        self.model.load()
    def button5_click(self):
        c=[]
        self.text = ''

        for i in range(len(self.model.predict_array(self.path)[0])):
            e=0
            b = int(self.model.predict_array(self.path)[0][i] * 1000000)
            e = b / 10000
            c.insert(i,e)
            self.text = str(self.text)+str(self.modelnames[i])+": "+str(e)+'\n'


        self.text_label.setText(self.text)
    def button6_click(self):

        self.path, _=QFileDialog.getOpenFileName(self,'','.','All Images(*.*))')
        self.pixmap = QPixmap(str(self.path))
        self.image_label.setPixmap(self.pixmap)
        self.button5.setEnabled(True)


def a(cls,exception,traceback):
    sys.__excepthook__(cls,exception,traceback)


if __name__=='__main__':
    sys.excepthook = a

    app=QApplication(sys.argv)
    classification_ai= ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())

