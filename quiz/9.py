from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel,QHBoxLayout,QVBoxLayout, QGroupBox
import sys

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.sum=0
        self.setWindowTitle('제목')
        self.button1= QPushButton('-')
        self.button2 = QPushButton('+')
        self.button3 = QPushButton('^')
        self.button4 = QPushButton('^-')
        self.text_label = QLabel(self)
        self.text_label.setText('0')

        self.button1.clicked.connect(self.button1_click)
        self.button2.clicked.connect(self.button2_click)
        self.button3.clicked.connect(self.button3_click)
        self.button4.clicked.connect(self.button4_click)
        self.hbox_layout = QHBoxLayout()
        self.h2box_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)
        self.hbox_layout.addWidget(self.button3)
        self.hbox_layout.addWidget(self.button4)
        self.h2box_layout.addWidget(self.text_label)
        self.group_box1 = QGroupBox("그룹1")
        self.group_box2 = QGroupBox("그룹2")
        self.group_box1.setLayout(self.hbox_layout)
        self.group_box2.setLayout(self.h2box_layout)
        self.main_layout=QGridLayout()
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 6)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 6)
        self.setLayout(self.main_layout)

    def button1_click(self):
        self.sum-=1
        self.text_label.setText(str(self.sum))

    def button2_click(self):
        self.sum += 1
        self.text_label.setText(str(self.sum))

    def button3_click(self):
        self.sum = self.sum**2
        self.sum = int(self.sum)
        self.text_label.setText(str(self.sum))

    def button4_click(self):
        self.sum= self.sum**(1/2)
        self.sum=int(self.sum)
        self.text_label.setText(str(self.sum))


if __name__=='__main__':
    app=QApplication(sys.argv)
    classification_ai= ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())

