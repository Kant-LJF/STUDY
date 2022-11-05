#!/user/bin/env python
# _*_coding=utf-8_*_
''''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''
from typing import List
def majorityElement( nums: List[int]) -> int:
    dict = {}
    for key in nums:
        dict[key] = dict.get(key, 0) + 1
        # print(dict.get(key, 0))
    print(dict)
    for key, value in dict.items():
        if (value == max(dict.values())):
            return key


nums=[1,1,1,1,1,1,8]

print(majorityElement(nums))