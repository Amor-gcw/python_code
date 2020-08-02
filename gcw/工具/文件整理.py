# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
winston_GAI
20200731
文件整理，按照文件类型进行归类
'''

# 导入模块
import os
import shutil

#这里引号中输入待处理文件夹的路径
path=r' '#路径
files=os.listdir(path)

# for循环进行文件整理
for f in files:
    f = path + '/' + f
    if os.path.isfile(f):
        folder_name=path+f.split('.')[-1]
        print('move {} to {}'.format(f, folder_name))
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            shutil.move(f,folder_name)
        else:
            shutil.move(f,folder_name)