# !/usr/bin/env python3
# -*- coding: utf-8 -*-

### winston_gai
### 20200806
### 第三部分 函数

'''
def hello(): # 定义函数
    print('hello,world') #函数体，括号里面是参数
    print('coming here')

hello() # 调用函数,调用几次函数最终就会表达几次

3.1 def语句和参数
 def hello(name):
     print('hello ' + name)

 hello('lin')

3.2 返回值和return语句
import random # 导入模块
def getAnswer(answerNumber):# 定义getanwser函数
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

answerNumber= random.randint(1,9)
output = getAnswer(answerNumber)
print(output)

 3.3 None值
 python中的None值表示没有值，是NoneType数据类型的唯一值，在其他的编程语言中，可能称这个值为null、nil、undefined


'''

spam = print('hello')
