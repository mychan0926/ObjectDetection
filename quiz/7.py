from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QHBoxLayout,QGroupBox
import sys

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.button1 = QPushButton('버튼 1')
        self.button2 = QPushButton('버튼 2')
        self.button3 = QPushButton('버튼 3')
        self.button4 = QPushButton('버튼 4')
        self.button5 = QPushButton('버튼 5')
        self.button6 = QPushButton('버튼 6')
        self.button7 = QPushButton('버튼 7')
        self.button8 = QPushButton('버튼 8')

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.button7)
        self.vbox_layout.addWidget(self.button8)

        self.hbox_layout=QVBoxLayout()
        self.hbox_layout.addWidget(self.button4)
        self.hbox_layout.addWidget(self.button5)
        self.hbox_layout.addWidget(self.button6)
        self.main_layout=QGridLayout()

        self.v1box_layout = QHBoxLayout()
        self.v1box_layout.addWidget(self.button1)
        self.v1box_layout.addWidget(self.button2)
        self.v1box_layout.addWidget(self.button3)

        self.group_box1 = QGroupBox("그룹1")
        self.group_box2 = QGroupBox("그룹2")
        self.group_box3 = QGroupBox("그룹3")

        self.group_box1.setLayout(self.v1box_layout)
        self.group_box2.setLayout(self.hbox_layout)
        self.group_box3.setLayout(self.vbox_layout)
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 4)
        self.main_layout.addWidget(self.group_box2,2,0,1,2)
        self.main_layout.addWidget(self.group_box3,2, 2, 1, 2)

        self.setLayout(self.main_layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    classification_ai= ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())


