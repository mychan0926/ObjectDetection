from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QHBoxLayout
import sys

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.button1=QPushButton('버튼 1')
        self.button2 = QPushButton('버튼 2')
        self.button3 = QPushButton('버튼 3')
        self.button4 = QPushButton('버튼 4')
        self.button5 = QPushButton('버튼 5')
        self.button6 = QPushButton('버튼 6')
        self.button7 = QPushButton('버튼 7')
        self.button8 = QPushButton('버튼 8')
        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.button3)
        self.vbox_layout.addWidget(self.button4)

        self.hbox_layout=QVBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)
        self.hbox_layout.addWidget(self.button8)
        self.main_layout=QGridLayout()


        self.main_layout.addWidget(self.button5, 0, 0, 1, 2)
        self.main_layout.addWidget(self.button6, 0, 2, 1, 2)
        self.main_layout.addWidget(self.button7, 0, 4, 1, 2)

        self.main_layout.addLayout(self.hbox_layout,1,0,1,3)
        self.main_layout.addLayout(self.vbox_layout,1, 3, 1, 3)

        self.setLayout(self.main_layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    classification_ai= ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())


