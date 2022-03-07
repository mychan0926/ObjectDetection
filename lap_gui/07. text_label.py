from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout
import sys

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.text_label=QLabel(self)
        self.text_label.setText('텍스트')


        self.hbox_layout=QVBoxLayout()
        self.hbox_layout.addWidget(self.text_label)
        self.main_layout=QGridLayout()
        self.main_layout.addLayout(self.hbox_layout,0,0,1,1)

        self.setLayout(self.main_layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    classification_ai= ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())

