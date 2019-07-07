# -*- coding: UTF-8 -*-

# Filename : 01-string.py23
# author by : Steven Lu

# 目的:
# 列表和元组
print("开始")

import random

List1 = ['张飞','赵云','马超','吕布']
Tup1 = ('刘备','曹操','孙权')

pos = 0
value = List1[pos]
print("取出列表的第%d个值，它是%s"%(pos,value))

print ("输出列表中所有元素")
pos = 0
for v in List1:
    print ("取出列表的第%d个值，它是%s"%(pos,v))
    pos = pos + 1

print("开始")
newvalue = '关羽'
List1[0] = newvalue
print("取出列表的第%d 个值， 它是%s"%(pos,v))
pos = 0
for v in List1:
    print ("取出列表的第%d个值，它是%s"%(pos,v))
    pos = pos + 1

print("开始")
for i in range(1,5):
    s= random.choice(List1)
    print(s)
