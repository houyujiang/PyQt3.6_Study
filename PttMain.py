# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      PttMain
   Description :
   Author :        houyujiang
   date：           2018/1/25 11:08
   IDE:             PyCharm
-------------------------------------------------
   Change Activity:
                   2018/1/25:
-------------------------------------------------
"""
import sys
from PyQt5 import QtWidgets
from pttUI import Ui_MainWindow
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class myform(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(myform, self).__init__()
        self.setupUi(self)
        #设置一个4*4的表格数据模型
        self.model = QStandardItemModel(4, 4)
        #设置横坐标每项的属性名
        self.model.setHorizontalHeaderLabels(['id', '分组码', '东经', '北纬'])
        #配置数据，注意！！！需要使用QStandardItem格式的文本
        self.model.setItem(0, 0, QStandardItem('0000'))
        self.model.setItem(0, 1, QStandardItem('0000'))
        self.model.setItem(0, 2, QStandardItem('108.1721'))
        self.model.setItem(0, 3, QStandardItem('20.1231'))
        self.model.setItem(1, 0, QStandardItem('189'))
        self.model.setItem(1, 1, QStandardItem('1001'))
        self.model.setItem(1, 2, QStandardItem('108.1721'))
        self.model.setItem(1, 3, QStandardItem('20.1231'))
        self.model.setItem(2, 0, QStandardItem('175'))
        self.model.setItem(2, 1, QStandardItem('1002'))
        self.model.setItem(2, 2, QStandardItem('108.1721'))
        self.model.setItem(2, 3, QStandardItem('20.1231'))
        self.model.setItem(3, 0, QStandardItem('152'))
        self.model.setItem(3, 1, QStandardItem('1003'))
        self.model.setItem(3, 2, QStandardItem('108.1721'))
        self.model.setItem(3, 3, QStandardItem('20.1231'))
        self.tableView.setModel(self.model)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = myform()
    ex.show()
    sys.exit(app.exec_())

