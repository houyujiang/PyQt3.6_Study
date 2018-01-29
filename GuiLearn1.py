# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      GuiLearn1
   Description :
   Author :        houyujiang
   date：           2018/1/23 10:28
   IDE:             PyCharm
-------------------------------------------------
   Change Activity:
                   2018/1/23:
-------------------------------------------------
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('simple')
    w.show()
    c = QWidget()
    c.resize(250, 250)
    c.move(600, 600)
    c.setWindowTitle('two-simple')
    c.show()
    sys.exit(app.exec_())