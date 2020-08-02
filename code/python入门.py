# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    editor: gcw
    data: 20200313
    < python入门学习 >
"""

# 变量（标识符）
# file = open('gcw.txt', 'w') 打开gcw.txt文件，w代表若无此文件则自动创建此文件
# file.write('hello,world')   打开后自动输入’hello，world‘


# 字符串的基本用法
# 字符串就是在'' / "”之间的文字或字母

# word = 'a loooooong word'
# print(len(word))

# word = 'friends'
# find_the_evil_in_your_friends = word[0]+word[2:4]\
#                                 +\
#                                 word[-3:-1] # 代码太长，可以使用\换行
# print(find_the_evil_in_your_friends)
#
# 字符串的方法（这里的方法指的是对象的特征和功能）
# phone_number = '12196417000'
# show_number = phone_number.replace(phone_number[0:9], '*' * 9)
# print(show_number)


# search = '569'
# num_a = '15615356980'
# num_b = '15615569790'
# first_num_1 = search + ' is at ' + str(num_a.find(search)) + ' to ' + \
#             str(num_a.find(search) + len(search)) + ' of num_a'
# first_num_2 = search + ' is at ' + str(num_b.find(search)) + ' to ' + \
#             str(num_b.find(search) + len(search)) + ' of num_b'
# print(first_num_1)
# print(first_num_2)


# print('{} a word she can get what she {} for.'.format('With', 'came'))
# print('{preposition} a word she can get what she {verb} for'.format(preposition = 'With', verb = 'came'))
# print('{0} a word she can get what she {1} for.'.format('With', 'came'))

# 定义函数
# def function (arg参数1，arg参数2）:
#    return 'something'
# 在缩进后的语句被称为语句块（block)，缩进是为了表明语句和逻辑的从属关系。

# def fa_converter(C):
#     fa = C * 9/5 + 32
#     return str(fa) + '°F'
# C_to_F = fa_converter(10)
# print(C_to_F)
"""
定义一个函数--fa_converter(C),输入内容C作为参数，最后返回的是华氏度，
函数定义结束后，我们就可以调用函数了，既像函数发出指令，并得到结果

"""
# 练习
# 设置一个重量转换器，输入'g'为单位的数字，返回’KG‘结果。
# 设计一个求指教三角形斜边长的函数（两条直角边为参数，求最长边）
"""
1、传递参数与参数类型
 1.1传递参数的方式有两种：
  （1）位置参数
    填入的参数对应着固定的变量，这种传入参数的方式被称为位置参数
    
  （2）关键词参数
    在调用函数时，我们将每一个参数名称后面直接赋予一个我们想要传入的值，
    这种以名称作为一一对应的参数传入方式被城作为关键词参数
    
"""


