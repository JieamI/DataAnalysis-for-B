# !/usr/bin/env python
# Author: Caijie Fan
# Module name: main_query
from Info_query import Av_query, Up_query

flag = input('(0：视频数据查询 1：up主数据查询)\n请选择查询数据类型：')
if flag == '0':
    av = input('请输入要查询视频的av号：')
    # Av_query('412935552').renderData()
    Av_query(av).renderData()
    print('查询成功，数据文件已存入当前目录的Info_query文件夹下！')
elif flag == '1':
    uid = input('请输入要查询up主的uid：')
    # Up_query('517327498').renderData()
    Up_query(uid).renderData()
    print('查询成功，数据文件已存入当前目录的Info_query文件夹下！')
else:
    print('请输入0/1查询！')
