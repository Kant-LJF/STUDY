#!/user/bin/env python
# _*_coding=utf-8_*_
class Solution():

    def twoSum(self, nums, target) :
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={}
        k = len(nums)
        for i in range(0, k):   #一边将列表中的数添加到字典中，一边判断两数之差是否存在于字典中
            temp = target - nums[i]
            if temp in map :  # 判断步骤
                print(map)
                return [map[temp],i]
            map[nums[i]]=i




if __name__ == '__main__':
    nums = [3,4,2]
    target = 6
    print(Solution().twoSum(nums,target))