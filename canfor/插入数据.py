#!/user/bin/env python
# _*_coding=utf-8_*_

"""
已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：
[3, 5, 1, 7]
"""
a = [1, 3, 5, 7]
# insert 插入数据
a.insert(3, a[0])
print(a[1:])
print(a)