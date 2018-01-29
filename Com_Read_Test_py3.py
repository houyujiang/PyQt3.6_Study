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

def read_Com():
    serials = serial.Serial('Com3',115200)
    argv = serials.read(40)
    argv = ''
    argv = argv.encode('utf-8')
    print(argv)
    print(type(argv))

    result = ''
    hlen = len(argv)
    for i in range(hlen):
        hvol = ord(argv[i])
        hhex = '%02x' % hvol
        result += hhex + ''
    print(result)
if __name__ == '__main__':
    read_Com()