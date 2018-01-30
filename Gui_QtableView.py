# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 1:02
# @Author  : houyujiang
# @Email   : houyujiang@live.cn
# @File    : Gui_QtableView.py
# @Software: PyCharm
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Table(QWidget):
    def __init__(self,arg = None):
        super(Table,self).__init__(arg)
        self.setWindowTitle('QTbaleView表格试图控件')
        self.resize(640,480)
        self.tableView = QTableView()
        dlgLayout = QVBoxLayout()
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)
    def setModel(self):
        self.model = QStandardItemModel(3, 5)#列，行
        self.model.setHorizontalHeaderLabels(['id', '分组码', '经度', '维度', '海拔'])
        list = [['120','0001','186.1225','34.5625','400'],['137','0002','186.1225','34.5625','700'],['187','0003','186.1225','34.5625','600']]
        for row in range(3):
           for column in range(5):
               print(row,column,type(row))
               items = QStandardItem('%s'%list[row][column])
               self.model.setItem(row,column,items)
        self.tableView.setModel(self.model)
        print('a')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = Table()
    table.setModel()
    table.show()
    sys.exit(app.exec_())