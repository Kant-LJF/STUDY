#!/user/bin/env python
# _*_coding=utf-8_*_
#斐波那契数列 解法1  递归
def fib(n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:return 1
        if n==2: return 1
        return fib(n-1)+fib(n-2)


class Solution():
    def fib(self, n: int) -> int:
        # 做三个变量c=a+b，a=b，b=c，最后取模
        if n == 0 or n == 1:
            return n
        a, b, c = 0, 1, 0
        for _ in range(n-1):
            c = a + b
            a = b
            b = c
        c %= 1000000007
        return c


n = int(input().strip())
# print(fib(n))
print(Solution().fib(n))


