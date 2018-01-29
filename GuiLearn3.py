# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      GuiLearn3
   Description :
   Author :        houyujiang
   date：           2018/1/23 11:38
   IDE:             PyCharm
-------------------------------------------------
   Change Activity:
                   2018/1/23:
-------------------------------------------------
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 10
        y = 0
        self.text = "x:{0},y:{1}".format(x,y)
        self.label= QLabel(self.text,self)
        grid.addWidget(self.label,0,0,Qt.AlignTop)
        self.setMouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(300,300,350,200)
        self.setWindowTitle('Event Object')
        self.show()
    #捕捉鼠标动作获取坐标
    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        print(type(x))
        text ="x:{0},y:{1}".format(x,y)
        print (text)
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())