# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      Com_Read_Test_py3
   Description :
   Author :        houyujiang
   date：           2018/1/25 17:34
   IDE:             PyCharm
-------------------------------------------------
   Change Activity:
                   2018/1/25:
-------------------------------------------------
"""
import serial
import re
com = serial.Serial('Com3',115200)
bytea = com.read(40)
str = bytea.hex()
print (str)