#!/user/bin/env python
# _*_coding=utf-8_*_
"""
更有效率的方法（当然，仅对此题而言，效率是无所谓的）是：不断地除10取余。
下面用取余法再来一遍：
"""
def is_shui_xian(n):
	if n < 100 or n > 999: return False
	sum = 0
	n1 = n
	while n1 > 0:
		sum += (n1 % 10) ** 3
		n1 //= 10 #表示n除以10的结果向下取整
	return n == sum

if __name__ == '__main__':
	for i in range(100,1000):
		if is_shui_xian(i): print(i)
