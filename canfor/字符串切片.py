#!/user/bin/env python
# _*_coding=utf-8_*_
#字符串 "axbyczdj"，如果得到结果“abcd”

str="axbyczdj"
list=[]
for i in range(0,len(str)):
    if i%2==0:
        list.append(str[i])

print("".join(list))

a = "axbyczdj"
print(a[::2])
print(a[::3])
print(a[::-1])