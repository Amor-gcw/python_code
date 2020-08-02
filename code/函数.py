# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    函数练习
    gai_chaowei
    20200317
"""

# 1、设置一个重量转换器，输入'g'为单位的数字，返回’kg‘结果。
"""
思路：首先我们应该定义一个函数，输入参数并返回转换完成的结果，
注意在输入过程中数字与字符串的转换以及输出界面的优化
"""
# def weight_converter(g):
#     kg = g/1000
#     return int(kg)
# weight_message = input('请输入以 g 为单位的重量: ')
# kg_message = weight_converter(int(weight_message))
# print('转换后重量为: ' + str(kg_message) + 'kg')



# 2、设计一个求直角三角形斜边长的函数（两条直角边为参数，求最长边）
"""
思路：先定义一个用来求边长的函数，其中涉及到两个参数，在调用函数时，注意同时输入两个参数（位置参数）
"""
# def hypo_converter(L1, L2):
#     hypo_number = (L1**2 + L2**2)**0.5
#     return int(hypo_number)
#
# L_message_1 = input('请输入第一条直角边长度： ')
# L_message_2 = input('请输入第二条直角边长度： ')
# hypo = hypo_converter(int(L_message_1), int(L_message_2))
# print('斜边长是：' + str(hypo))

