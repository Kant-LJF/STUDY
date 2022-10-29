#!/bin/python3

import math
import os
import random
import re
import sys
import json
import requests


#
# Complete the 'getUsernames' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER threshold as parameter.
# API URL: https://jsonmock.hackerrank.com/api/article_users?page=<pageNumber>
# user and articles

def getUsernames(threshold):
    # Write your code here
    list = []
    for i in range(1, threshold + 1):
        r = requests.request('GET', 'https://jsonmock.hackerrank.com/api/article_users?page=', params=i).json()
        for j in range(0, len(r["data"]) ):

            if r["data"][j]["submission_count"] > threshold:

                print(r["data"][j]["username"])
                list.append(r["data"][j]["username"])

            for k in list:  #剔除重复 其实不剔除好像也可以
                if k not in list: list.append(k)
            if len(list) > threshold-1:
                break;
        if len(list) > threshold-1:
            break;
    return list


if __name__ == '__main__':


    threshold = int(input().strip())

    result = getUsernames(threshold)
    print(result)



