#!/user/bin/env python
# _*_coding=utf-8_*_
from typing import List


def single_number(nums: List[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    n = [1, 2, 2, 45, 54, 54, 45]
    print(single_number(n))
