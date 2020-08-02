# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
winston_gai
20200801
python 控制流

1 布尔值(True/False)
布尔值用于表达式中，并且可以保存在变量中，书写时注意大小写

2 比较操作符
  == 等于
  ！= 不等于

  < 小于
  > 大于
  <= 小于等于
  >= 大于等于
    < > <= >= 操作符仅适用于整型和浮点型值

3 布尔操作符 (and/or/not)
 布尔操作符也有操作顺序，python先计算not操作符，后计算and操作符，然后计算or操作符
 3.1 二元布尔操作符
  and 和 or 总是能接受两个布尔值或表达式，所以被认为是'二元‘操作符。
  and真值表中，只要有一个布尔值为False 结果就是False
  or真值表中，只要有一个布尔值为Ture,结果就是Ture
 3.2 not操作符
  not操作符只作用于一个布尔值或表达式，结果为相反的布尔值
 3.3 混合布尔和比较操作符
  exam：
  (4<5) and (5<6) T
  (1==2) or (2==2) F

4 控制流元素
 4.1 条件
 控制流语句根据条件是T or F,来决定做什么，几乎所有的控制流语句都使用条件
 4.2 代码块
  一些代码可以成为一组，放在”代码块”中，可以根据代码行的缩进，知道代码块的开始和结束
  规则：
  （1）缩进增加时，代码块开始
  （2）代码块可以包含其他代码块
  （3）缩进减少为0，或减少为外面包围代码块的缩进，代码块就结束
 4.3 程序执行

5 控制流语句
所有的控制流语句都是以冒号结束，下一行缩进开始新的代码块

 5.1 if语句
 语句条件为T 时执行，F时跳过
 过程：
 if关键字：
 条件
 冒号：
    缩进的代码块（if子句）

 5.2 else语句
 只有在if语句执行为F时，才会执行else语句

 5.3 elif语句
 在多重要求的条件下，会用到elif语句，总是跟在if语句或者上一个elif语句后面

 5.4 while循环语句
 利用while循环语句，可以让代码块重复执行，只要循环语句条件为T即可
 不同于if语句，if语句子句结束后程序执行if语句之后的语句，但在while循环中，程序循环跳回到while语句开始处
 5.5 break 语句
 break语句可以提前跳出while循环语句，如果执行遇到break语句，就会立马推出while语句，在代码中，仅包含break关键字
 exam:
 while T:
    print('please type your name')
    name= input('请输入你的名字')
    if name == 'your name':
        break
 print('程序结束')
 5.5 continue 语句
 continue语句用于循环内部，如果程序执行遇到continue语句，就会马上跳回循环处开始，重新对循环条件求值（这也是执行到达循环末尾时发生的事情）\

 5.6 for循环和range()函数
 通过for循环和range()函数，使得函数执行固定次数


'''



# name = ' '
# while name != 'your name':
#     print('please type your name')
#     name= input('输入名字： ')
# print('程序结束！')

# name = ' '
# while name != 'your name':
#     print('please type your name')
#     name = input('请输入你的名字')
#     if name == 'your name':
#         break
# print('程序结束')

# while True:
#     print('who are you?')
#     name = input('请输入你的名字')
#     if name == '':
#         continue
#     print('请输入密码:')
#     password= input('')
#     if password == '0000':
#         break
# print('welcome')


name= ''
while name=='':
    print('请输入你的名字:')
    name = input()
    print('有多少客人呢？')
    guestnumber = input()
    if guestnumber:
        print('我们将准备{}间房间供客人使用'.format(guestnumber))
    print('欢迎下次光临')













