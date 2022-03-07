from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGridLayout, QFileDialog
import sys
import os
class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.button1=QPushButton('파일 열기..')
        self.button1.clicked.connect(self.button1_click)
        self.hbox_layout=QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)

        self.main_layout=QGridLayout()
        self.main_layout.addLayout(self.hbox_layout,0,0,1,1)

        self.setLayout(self.main_layout)
    def button1_click(self):
        path, _=QFileDialog.getOpenFileNames(self,'','.','All Files(*.*))')#값 2개 가져와서 1개 버림 (1,2,3,4,5) (1,창제목,경로,필터링(2개 이상이면 공백으로 구분. *.py *.cpp))
        #오류 확인용         for i in range (len(path)):
        #오류 확인용             f = open(path[i], 'r',encoding='utf-8')ㄴ
        #오류 확인용             line = f.read()
        #오류 확인용             print(line)

        #오류 확인용         f.close()

#오류 확인용 def a(cls,exception,traceback):
#오류 확인용     sys.__excepthook__(cls,exception,traceback)
if __name__=='__main__':
    #오류 확인용     sys.excepthook= a
    app=QApplication(sys.argv)
    classification_ai= ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())



