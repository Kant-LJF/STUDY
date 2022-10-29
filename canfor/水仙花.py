#!/user/bin/env python
# _*_coding=utf-8_*_
sxh = []
for i in range(100, 1000):

  s = 0
  m = list(str(i))  #三位数 弄成list 方便遍历
  for j in m:
   s += int(j)**len(m)  #遍历出来的数字进行立方然后加起来

   if i == s:
    print(i)
   sxh.append(i)
print("100-999 的水仙花数：%s" % sxh)


