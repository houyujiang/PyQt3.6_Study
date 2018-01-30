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
'''
出现的问题：
    使用in_waiting读取字符长度，再传入read()读取内容时，无法使用int('',10)进行进制转换。
'''
import serial
import re
import  time
def com_factory():
    com = serial.Serial('Com3',115200)
    #time.sleep(1)
    #len= com.in_waiting
    #print ('读取到的字符长度：',len)
    str = com.read(40)
    str = str.hex()
    #print('读取到的结果',str)
    return str

#分解成两两一组的16进制字符
def fen_jie_str(str):
    fen_jie_after = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", str)
    return fen_jie_after

#id转换,16进制转换10进制
def cover_id(str):
    id_orginal = str[6:12]  # 截取id
    id_cover = int(id_orginal,16)
    return id_cover

def cover_fenzuma(str):
    fenzuma_orginal = str[18:22]  # 截取id
    fenzuma_cover = int(fenzuma_orginal, 16)
    return fenzuma_cover

#转换昵称
def cover_nicheng(str):
    pass

#获取目标地址(获取没任何意思)
def cover_mubiao_dizhi(str):
    mubiaodizhi_org = str[12:18]
    mubiaodizhi = int(mubiaodizhi_org,16)
    return mubiaodizhi

#转换经度坐标
def cover_jindu(str):
    east_org = str[54:62]
    #print(east_org)
    east_list = [east_org[6:8], east_org[4:6], east_org[2:4], east_org[0:2]]
    east_str = ''.join(east_list)
    east_num = int(east_str,16)
    east_zuobiao = east_num/float(1000000)
    return east_zuobiao

#转换维度坐标
def cover_weidu(str):
    north_org = str[64:72]
    print(north_org)
    north_list = [north_org[6:8], north_org[4:6], north_org[2:4], north_org[0:2]]
    north_str = ''.join(north_list)
    north_num = int(north_str, 16)
    north_zuobiao = north_num / float(1000000)
    return north_zuobiao

#转换海拔高度
def cover_haiba(str):
    haiba_org = str[72:76]
    haiba_list = [haiba_org[2:4],haiba_org[0:2]]
    haiba_str = ''.join(haiba_list)
    haiba_num = int(haiba_str,16)
    haiba_height = haiba_num/float(10)
    return haiba_height

#读取设备状态
def cover_state(str):
    pass

if __name__ == '__main__':
    while True:
        com_str = com_factory()
        fenjie_str = fen_jie_str(com_str)
        id = cover_id(com_str)
        fenzuma = cover_fenzuma(com_str)
        east = cover_jindu(com_str)
        north = cover_weidu(com_str)
        haiba = cover_haiba(com_str)
        mubiao = cover_mubiao_dizhi(com_str)
        print ('分解：',fenjie_str)
        print('id：',id)
        print('分组码：',fenzuma)
        print('东经：',east)
        print('维度',north)
        print('海拔高度',haiba)
        print('目标地址：',mubiao)