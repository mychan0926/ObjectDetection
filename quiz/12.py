from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel,QHBoxLayout,QVBoxLayout, QGroupBox,QFileDialog,QTabWidget
from PyQt5.QtGui import QPixmap
import sys
import model
import cv2
import os
import yolov3
class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.image_label=QLabel(self)
        self.model = model.Model()

        self.modelnames=self.model.class_name()

        print(self.modelnames)

        self.setWindowTitle('이미지 분류 AI')

        self.button1=  QPushButton('이미지 선택')

        self.group_box1 = QGroupBox("메뉴")
        self.group_box2 = QGroupBox("원본 이미지")
        self.group_box3 = QGroupBox("사물 검출 결과")

        self.text_label = QLabel(self)
        self.text_label.setText('')
        self.hbox_layout=   QHBoxLayout()
        self.v1box_layout = QVBoxLayout()
        self.v2box_layout = QVBoxLayout()
        self.button1.clicked.connect(self.button1_click)
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addStretch(1)
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
        self.path, _ = QFileDialog.getOpenFileName(self, '', '.', 'All Images(*.*))')
        self.pixmap = QPixmap(str(self.path))
        self.image_label.setPixmap(self.pixmap)

class ClassificationAI_mp(QWidget):
    def __init__(self):
        super().__init__()
        self.image_label=QLabel(self)
        self.model = model.Model()

        self.modelnames=self.model.class_name()

        print(self.modelnames)

        self.setWindowTitle('영상 분류 AI')

        self.button1=  QPushButton('영상 선택')

        self.group_box1 = QGroupBox("메뉴")
        self.group_box2 = QGroupBox("영상")
        self.text_label = QLabel(self)
        self.text_label.setText('')
        self.hbox_layout=   QHBoxLayout()
        self.v1box_layout = QVBoxLayout()
        self.v2box_layout = QVBoxLayout()
        self.button1.clicked.connect(self.button1_click)
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addStretch(1)
        self.v2box_layout.addWidget(self.text_label)
        self.v1box_layout.addWidget(self.image_label)
        self.group_box1.setLayout(self.hbox_layout)
        self.group_box2.setLayout(self.v1box_layout)
        self.main_layout=QGridLayout()
        self.main_layout.addWidget(self.group_box1,0,0,1,2)
        self.main_layout.addWidget(self.group_box2, 1, 0, 5, 1)
        self.setLayout(self.main_layout)

    def button1_click(self):
        self.path, _ = QFileDialog.getOpenFileName(self, '', '.', 'All Video(*.*))')



def a(cls,exception,traceback):
    sys.__excepthook__(cls,exception,traceback)


class RoadObjectDetectionAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('도로 객체 검출 AI')


        classification_ai_tab_mp = ClassificationAI_mp()
        classification_ai_tab = ClassificationAI()
        tabs = QTabWidget()
        tabs.addTab(classification_ai_tab_mp, '동영상')
        tabs.addTab(classification_ai_tab, '이미지')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rod_ai = RoadObjectDetectionAI()
    rod_ai.show()
    sys.exit(app.exec_())
