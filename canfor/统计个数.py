#!/user/bin/env python
# _*_coding=utf-8_*_
"""
统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1,
-9, -4, -5, 8]
"""
count=0
a=[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
for i in a:
    if i >0: count+=1
print(count)


#生成器 variable    =    [out_exp    for    out_exp    in    input_list    if    out_exp    ==    2]
b = [i for i in a if i > 0]
print("大于 0 的个数：%s" % len(b))
c = [i for i in a if i < 0]
print("小于 0 的个数：%s" % len(c))