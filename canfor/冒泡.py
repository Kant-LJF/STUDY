#!/user/bin/env python
# _*_coding=utf-8_*_
arr = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(arr)):
    for j in range(0,len(arr)-1):  #从大到小可以减去i提高效率
        if arr[j] < arr[j+1]:
            arr[j+1],arr[j]=arr[j],arr[j+1]
print(arr)