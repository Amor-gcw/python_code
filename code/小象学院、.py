# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#定义变量

# milktea_name= "奶茶"
# milktea_numbe= 1
# milktea_price= 7
# milktea_quantity=1
# total_money=(milktea_numbe*milktea_price*milktea_quantity)
# vip_money=total_money*0.9
# print(vip_money)


# milktea_name= input('请输入奶茶编号：')
#
# if int(milktea_name) == 1:
#     milktea_price = 3
# elif int(milktea_name) == 2:
#     milktea_price = 5
# else:
#     print('奶茶编号有误')
# print(milktea_price)


# milktea_num = 4
# if 1<= milktea_num <= 5:
#     print('奶茶编号输入正确。')
#     if milktea_num == 1:
#         price = 7
#         print('奶茶的价格是{}。:'.format(price))
#     elif milktea_num == 2 or milktea_num == 3:
#         price = 5
#         print('奶茶的价格是{}。:'.format(price))
#     else:
#         print('奶茶的价格是10元。')
#
# else:
#     print('Woops!我们只售卖以上五种奶茶哦！新口味敬请期待！')

# # 定义变量
# num1 = 4
# num2 = 2
# # 条件语句
# if num1 != 0:
#     output = num2/num1
#     print(str(output))
# else:
#     print('除数为0，除法不合法')


# milktea_name = '蒟蒻冰奶茶'
# milktea_number = 4
# milktea_price = 7
# milktea_quantity = 1
# total_money = milktea_price * milktea_quantity
# print('您购买的是{}奶茶,共购买{}杯,总计{}元'.format(milktea_number, milktea_quantity, total_money))
# total_money *= 0.9
# print('您可以享受会员价格,折后价:{}元'.format(total_money))

# # 定义变量并赋值
# score = 84
# # 进入条件判断
# if score>=0 and score<72:
#     message = "很抱歉，你被淘汰了。"
# elif 72<= score <= 94:
#     message = "恭喜你，进入下一轮海选。"
# elif 94 <=score <= 100:
#     message = '恭喜你，直接进入好声音正赛。'
# else:
#     print('你的分数错误，请联系节目组核实分数。')
#
# print(message)

# print('****************************************')
# print('欢迎光临小象奶茶馆！\n小象奶茶馆售卖宇宙无敌奶茶!\n奶茶虽好，可不要贪杯哦！\n每次限尝鲜一种口味：\n1. 原味冰奶茶 3元 \n2. 香蕉冰奶茶 5元 \n3. 草莓冰奶茶 5元  \n4. 蒟蒻冰奶茶 7元  \n5. 珍珠冰奶茶 7元 ')
# print('****************************************')
# milktea_num = int(input('请选择您要购买的奶茶编号：'))
# milktea_quantity = int(input('请输入您要购买的数量：'))
# if_vip = input('您是小象奶茶馆的会员吗（y/n）？')
# if milktea_num <= 5 and milktea_num >= 1:
#     if milktea_num == 1:
#         price = 3
#     elif milktea_num == 2 or milktea_num == 3:
#         price = 5
#     elif milktea_num == 4 or milktea_num == 5:
#         price = 7
#     money = price * milktea_quantity
#     print('您购买的是{}号奶茶，共购买{}杯，总计{}元'.format(milktea_num, milktea_quantity, money))
#     if if_vip == 'y':
#         discount = float(input('今天你可以自定义会员折扣，请输入一个0到1之间的数字：'))
#         if discount >=0 and discount <= 1:
#             money *= discount
#             print('您可以享受会员价，折扣为：{}折，折后总价：{}元'.format(discount*10, money))
#         else:
#             money *= 0.9
#             print('您的折扣输入有误，本次消费还按照会员正常折扣9折，折后总价：{}元'.format(money))
#     elif if_vip == 'n':
#         print('不好意思哦，您目前还不是我们的会员，\n本次无法享受会员价喽，永远爱你么么哒！')
#     else:
#         print('我还是个小宝宝，您的输入我看不懂，您拿着小票问问小象君吧！')
# else:
#         print('Woops!我们只售卖以上五种奶茶哦！新口味敬请期待！')
# print('****************************************')
# print('做一枚有态度、有思想的奶茶馆（傲娇脸）！\n\t祝您今日购物愉快！\n\t\t诚挚欢迎您再次光临！')
# print('****************************************')



# score_str = int(input('请输入李雷的考试成绩：（注意考试成绩只能输入正整数）'))
# # 进入if循环
# if 90<= score_str:
#     output = '奖励一部苹果手机'
# elif 70<= score_str < 90:
#     output = '奖励一部小米手机'
# else:
#     output = "罚做200个俯卧撑"
#
# print(output)


# has_ticket = input('是否有车票，有请输入y，没有请输入n:  ')
# if has_ticket == "y":
#     print('请开始安检')
#     knife_length = input('是否携带刀具 ，是请输入yes，否请输入no:  ')
#     if knife_length == "yes":
#         warning_message = float(input('请输入刀具长度，输入至小数点后一位:  '))
#
#         if warning_message >= 10:
#             print('不允许携带超过{}厘米的刀具上车'.format(warning_message))
#         else:
#             print('安检通过,祝您旅途愉快。')
#     else:
#         print('安检通过，祝您旅途愉快。')
#
# else:
#     print('无车票，不允许进入安检')




























































































