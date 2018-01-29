# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      PttButton
   Description :
   Author :        houyujiang
   date：           2018/1/22 16:52
   IDE:             PyCharm
-------------------------------------------------
   Change Activity:
                   2018/1/22:
-------------------------------------------------
"""
from MainWin import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import serial
import binascii
#串口工厂

class MyWindows(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(MyWindows,self).__init__()
        self.setupUi(self)
    def btn_click(self):
        s = serial.Serial('com3', 115200)
        d = bytes.fromhex('68 02 09 01')
        print(d)
        s.write(d)
        self.textEdit.setText("hi,对讲已打开")

    def btn_click1(self):
        s = serial.Serial('com3', 115200)
        d = bytes.fromhex('68 02 09 00')
        print(d)
        s.write(d)
        self.textEdit.setText("hi,对讲已关闭")
app = QtWidgets.QApplication(sys.argv)
window = MyWindows()
window.show()
sys.exit(app.exec_())
