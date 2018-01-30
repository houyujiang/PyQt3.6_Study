# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 1:30
# @Author  : houyujiang
# @Email   : houyujiang@live.cn
# @File    : list.py
# @Software: PyCharm
list = [['120','0001','186.1225','34.5625','400'],['137','0002','186.1225','34.5625','700'],['187','0003','186.1225','34.5625','600']]
for row in range(3):
    for column in range(5):
        a=int(column)
        b=int(row)
        s=list[b][a]
        print(s)
print(list[3,4])