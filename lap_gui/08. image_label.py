from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap
import sys

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.image_label=QLabel(self)
        pixmap=QPixmap("../data/images/3b59c8a5-f0b031cc.jpg")
        self.image_label.setPixmap(pixmap)


        self.hbox_layout=QVBoxLayout()
        self.hbox_layout.addWidget(self.image_label)
        self.main_layout=QGridLayout()
        self.main_layout.addLayout(self.hbox_layout,0,0,1,1)

        self.setLayout(self.main_layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    classification_ai= ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())

