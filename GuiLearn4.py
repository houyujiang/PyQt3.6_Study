# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      GuiLearn4
   Description :
   Author :        houyujiang
   date：           2018/1/23 13:50
   IDE:             PyCharm
-------------------------------------------------
   Change Activity:
                   2018/1/23:
-------------------------------------------------
"""
#有时候我们会想知道是哪个组件发出了一个信号，PyQt5里的sender()方法能搞定这件事
import sys
from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton("Button 1",self)
        btn1.move(30,50)

        btn2 = QPushButton("Button 2",self)
        btn2.move(150,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300,300,290,150)

        self.setWindowTitle("Event sender")
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text()+'was pressd')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
