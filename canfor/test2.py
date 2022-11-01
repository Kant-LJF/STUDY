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
    for i in range(1, 3):
        r = requests.request('GET', 'https://jsonmock.hackerrank.com/api/article_users?page=%d'%i, params={}).json()
        for j in range(0, len(r["data"]) ):

            if r["data"][j]["submission_count"] > threshold:

                print(r["data"][j]["username"])
                if r["data"][j]["username"] not in list:
                    list.append(r["data"][j]["username"])

            if len(list) > threshold-1:
                break;
        if len(list) > threshold-1:
            break;
    return list

if __name__ == '__main__':


    threshold = int(input().strip())

    result = getUsernames(threshold)
    print(result)



