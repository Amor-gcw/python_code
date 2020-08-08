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
 range()对for循环进行迭代（默认从0开始）直到最后

 5.7 等价的while循环
 while可以做和for循环相同的事情，但是for更加简洁

 5.8 range()的开始、停止和步长参数
 range()可以调用多个参数，参数之间用”，“分割
 例如：
 for i in range(12,15):
    print(i)
 结果为 12 13 14
 利用range()计算步长，可以设置三个参数
 例如：
 for i in range(0,10,2)：
    print(i)
 (0,10,2)代表从0打10，中间以2为间隔
 结果是0，2，4，6，8
 也可以用负数作为步长参数进行递减

6 导入模块
 python内部可以调用一些基本的函数，称为”内建函数”。
 同样，也包含一些模块，成为“标准库“
 每个模块都是一个python程序，包含一些相关的函数，可以嵌入到程序之中，类似于R语言中的安装包
 导入模块使用import语句，主要包括：
 （1）import关键字
 （2）模块的名称
 （3）可选的更多模块，中间用逗号隔开
 # import random
 # for i in range(2):
 #     print(random.randint(90,100))

7 用sys.exit()提前结束程序
 默认情况下，程序执行到最后总会停止，但通过使用sys模块中得exit()函数可以提前终止程序运行
 如：

# import sys
# while True:
#     print("type exit to exit.")
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('you type '+ response + '.')

小结：
1、布尔数据类型有两种，分别为True 和 Flase
2、3个布尔操作符分别是 and/or/not
3、布尔操作值的真值表
4、6个比较操作符
    > < >= <= == !=
5、什么是条件，哪里可以使用条件
 条件是一个表达式，用于控制流语句中，表达结果为布尔值
6、break和continue的区别
 break是将执行移出循环，并接着循环执行，continue是将执行移到循环的开始


'''








































# print('my name is')
# i = 0
# while i < 5:
#     print('jim five times'+" "+str(i))
#     i +=1


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


# name= ''
# while name =='':
#     print('请输入你的名字:')
#     name = input()
#     print('有多少客人呢？')
#     guestnumber = input()
#     if guestnumber:
#         print('{},我们将准备{}间房间供客人使用'.format(name,guestnumber))
#     print('欢迎下次光临')

# total = 0
# for num in range(101): # 0--100
#     total = num +total # 计算0到100相加的总和
#     print(total)













