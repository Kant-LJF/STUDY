#!/user/bin/env python
# _*_coding=utf-8_*_
from typing import List

def searchMatrix( matrix: List[List[int]], target: int) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return True
    return False

matrix=[[-1,3]]
print(searchMatrix(matrix,3))